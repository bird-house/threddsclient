"""
Python objects for modelling a Thredds server
"""

from bs4 import BeautifulSoup as BSoup
from urllib import parse as urlparse
from .utils import size_in_bytes

import logging
logger = logging.getLogger(__name__)

FILE_SERVICE = ["HTTPServer"]
OPENDAP_SERVICE = ["OPENDAP", "OpenDAP"]
WMS_SERVICE = ["WMS"]
WCS_SERVICE = ["WCS"]


class Node(object):
    """
    Common items to all nodes
    """
    def __init__(self, soup, catalog):
        self.soup = soup
        self.catalog = catalog
        self.name = soup.get('name')
        self.content_type = None
        self.bytes = None
        self.modified = None

    def __repr__(self):
        return "<Node name: {0.name}, content type: {0.content_type}>".format(self)


class Service(Node):
    """
    A Thredds service
    """
    def __init__(self, soup, catalog):
        Node.__init__(self, soup, catalog)
        self.base = soup.get('base')
        self.url = urlparse.urljoin(self.catalog.url, self.base)
        self.service_type = soup.get('serviceType')
        self.content_type = "application/service"
        self.services = [Service(s, self.catalog) for s in soup.find_all('service', recursive=False)]


class CatalogRef(Node):
    """
    A reference to a different Thredds catalog
    """
    def __init__(self, soup, catalog):
        Node.__init__(self, soup, catalog)
        self.title = soup.get('xlink:title')
        self.name = self.title
        self.href = soup.get('xlink:href')
        self.url = urlparse.urljoin(self.catalog.url, self.href)
        self.content_type = "application/directory"

    def follow(self):
        from .client import read_url
        return read_url(self.url)


class Dataset(Node):
    """
    Abstract dataset class
    """
    def __init__(self, soup, catalog):
        Node.__init__(self, soup, catalog)

    def is_collection(self):
        return False

    @property
    def ID(self):
        return self.soup.get('ID')

    @property
    def url(self):
        return "{0}?dataset={1}".format(self.catalog.url, self.ID)

    @property
    def authority(self):
        authority = None
        if self.soup.get('authority'):
            authority = self.soup.get('authority')
        elif self.soup.metadata:
            authority = self.soup.metadata.authority
        elif self.soup.parent.metadata:
            authority = self.soup.parent.metadata.authority
        return authority

    @property
    def service_name(self):
        service_name = None
        if self.soup.servicename:
            service_name = self.soup.servicename.text
        elif self.soup.serviceName:
            service_name = self.soup.serviceName.text
        elif self.soup.metadata:
            if self.soup.metadata.serviceName:
                service_name = self.soup.metadata.serviceName.text
        elif self.soup.parent.metadata:
            if self.soup.parent.metadata.serviceName:
                service_name = self.soup.parent.metadata.serviceName.text
        return service_name

    @property
    def data_type(self):
        data_type = None
        if self.soup.get('datatype'):
            data_type = self.soup.get('datatype')
        elif self.soup.metadata:
            if self.soup.metadata.dataType:
                data_type = self.soup.metadata.dataType.text
        elif self.soup.parent.metadata:
            if self.soup.parent.metadata.dataType:
                data_type = self.soup.parent.metadata.dataType.text
        return data_type

    @property
    def data_format_type(self):
        data_format_type = None
        if self.soup.dataFormatType:
            data_format_type = self.soup.dataFormatType.text
        elif self.soup.metadata:
            if self.soup.metadata.dataFormatType:
                data_format_type = self.soup.metadata.dataFormatType.text
        elif self.soup.parent.metadata:
            if self.soup.parent.metadata.dataFormatType:
                data_format_type = self.soup.parent.metadata.dataFormatType.text
        return data_format_type


class CollectionDataset(Dataset):
    """
    A container for other datasets
    """
    def __init__(self, soup, catalog):
        Dataset.__init__(self, soup, catalog)
        self.collection_type = soup.get('collectionType')
        self.harvest = self._harvest(soup)
        # TODO: add attributes for harvesting: contributor, keyword, publisher, summary, rights, ...
        # see http://www.unidata.ucar.edu/software/thredds/current/tds/tutorial/CatalogPrimer.html#Describing_datasets
        self.content_type = "application/directory"
        from .catalog import find_datasets
        self.datasets = find_datasets(soup, self.catalog)
        from .catalog import find_references
        self.references = find_references(soup, self.catalog)

    def is_collection(self):
        return True

    @staticmethod
    def _harvest(soup):
        return soup.get('harvest', 'false') == 'true'


class DirectDataset(Dataset):
    """
    A reference to a data file
    """
    def __init__(self, soup, catalog):
        Dataset.__init__(self, soup, catalog)
        self.url_path = soup.get('urlPath')
        self.content_type = "application/netcdf"
        self.modified = self._modified(soup)
        self.bytes = self._bytes(soup)

    def access_url(self, service_type=FILE_SERVICE):
        url = None
        for service in self.catalog.get_services(self.service_name):
            if service.service_type in service_type:
                url = urlparse.urljoin(service.url, self.url_path)
                break
        return url

    def download_url(self):
        return self.access_url(FILE_SERVICE)

    def opendap_url(self):
        return self.access_url(OPENDAP_SERVICE)

    def wms_url(self):
        return self.access_url(WMS_SERVICE)

    @staticmethod
    def _modified(soup):
        modified = None
        if soup.date:
            if soup.date.get('type') == 'modified':
                modified = soup.date.text
        return modified

    @staticmethod
    def _bytes(soup):
        size = None
        if soup.dataSize:
            try:
                datasize = float(soup.dataSize.text)
                units = soup.dataSize.get('units')
                size = size_in_bytes(datasize, units)
            except Exception:
                logger.exception("dataset size conversion failed")
        return size
