"""
A Python view of a Thredds data server

http://www.unidata.ucar.edu/software/thredds/current/tds/tutorial/CatalogPrimer.html
"""

import logging
logger = logging.getLogger(__name__)

SKIPS = []


def flat_datasets(datasets):
    """
    Returns a list of all datasets in this catalog
    """
    flat_ds = []
    for ds in datasets:
        if ds.is_collection():
            flat_ds.extend(flat_datasets(ds.datasets))
        else:
            flat_ds.append(ds)
    return flat_ds


def flat_references(datasets):
    """
    Returns a list of references to other catalogs from this one
    """
    flat_refs = []
    for ds in datasets:
        if ds.is_collection():
            flat_refs.extend(ds.references)
            flat_refs.extend(flat_references(ds.datasets))
    return flat_refs


def find_references(soup, catalog):
    """
    Scans the soup to find references, then adds them to the catalog
    """
    from .nodes import CatalogRef
    references = []
    for ref in soup.find_all('catalogRef', recursive=False):
        title = ref.get('xlink:title', '')
        if any([x.match(title) for x in catalog.skip]):
            logger.info("Skipping catalogRef based on 'skips'.  Title: {0}".format(title))
            continue
        else:
            references.append(CatalogRef(ref, catalog))
    return references


def find_datasets(soup, catalog):
    """
    Scans the soup to find datasets, then adds them to the catalog
    """
    from .nodes import CollectionDataset, DirectDataset
    datasets = []
    for ds in soup.find_all('dataset', recursive=False):
        name = ds.get("name")
        if any([x.match(name) for x in catalog.skip]):
            logger.info("Skipping dataset based on 'skips'.  Name: {0}".format(name))
            continue
        elif ds.get('urlPath'):
            """
            THREDDS has no urlPath for collections
            """
            datasets.append(DirectDataset(ds, catalog))
        elif ds.find_all('access', recursive=False):
            """
            HYRAX has data access within sub elements
            """
            datasets.append(DirectDataset(ds, catalog))
        else:
            datasets.append(CollectionDataset(ds, catalog))
    return datasets


def skip_pattern(skip=None):
    """
    Creates a list of regular expression objects from a list of strings, used
    to exclude URLs from dataset lists
    """
    import re
    if skip is None:
        skip = SKIPS
    skip = map(lambda x: re.compile(x), skip)
    return skip


class Catalog:
    """
    A Thredds catalog

    TODO: use serverInfo to get harvest information
    http://www.esrl.noaa.gov/psd/thredds/serverInfo.xml
    """
    def __init__(self, soup, url, skip=None):
        self.soup = soup
        self.url = url
        self.skip = skip_pattern(skip)
        self._services = None
        self._references = None
        self._datasets = None

    @property
    def name(self):
        """
        The name of the catalog
        """
        name = self.soup.get('name')
        if not name and len(self.datasets) > 0:
            name = self.datasets[0].name
        if name:
            name = name.strip()
        return name

    @property
    def services(self):
        """
        List of service names supported by this catalog
        """
        if not self._services:
            from .nodes import Service
            self._services = [Service(x, self) for x in self.soup.find_all('service', recursive=False)]
        return self._services

    @property
    def references(self):
        """
        List of child references to other catalogs
        """
        if not self._references:
            self._references = find_references(self.soup, self)
        return self._references

    @property
    def datasets(self):
        """
        List of datasets and collections within this catalog
        """
        if not self._datasets:
            self._datasets = find_datasets(self.soup, self)
        return self._datasets

    def flat_datasets(self):
        """
        Flat list of datasets within this catalog
        """
        return flat_datasets(self.datasets)

    def flat_references(self):
        """
        Flat list of references within this catalog
        """
        flat_refs = []
        flat_refs.extend(self.references)
        flat_refs.extend(flat_references(self.datasets))
        return flat_refs

    def get_services(self, service_name):
        """
        Returns a list of services with names matching `service_name`
        """
        services = []
        for service in self.services:
            if service.name == service_name:
                if service.service_type.lower() == 'Compound'.lower():
                    services.extend(service.services)
                else:
                    services.append(service)
        return services

    def download_urls(self):
        """
        Returns a list of HTTP URLs used to download the raw data
        """
        urls = []
        for dataset in self.flat_datasets():
            urls.append(dataset.download_url())
        return urls

    def opendap_urls(self):
        """
        Returns a list of OpenDAP URLs used to access online data (e.g. with pydap)
        """
        urls = []
        for dataset in self.flat_datasets():
            urls.append(dataset.opendap_url())
        return urls
