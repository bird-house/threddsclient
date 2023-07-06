import pytest

from threddsclient import read_url


def test_noaa():
    # 'http://www.esrl.noaa.gov/psd/thredds/catalog.xml'
    # now directly redirects to 'https://psl.noaa.gov/thredds/catalog/catalog.xml'
    # therefore the name and returned references changed as well
    cat = read_url('http://www.esrl.noaa.gov/psd/thredds/catalog.xml')
    assert cat.name == 'THREDDS PSL Catalog'
    assert cat.url == 'http://www.esrl.noaa.gov/psd/thredds/catalog.xml'
    assert len(cat.references) == 3
    cat2 = cat.references[0]  # .follow()  # no need to follow anymore, since directly redirected
    assert cat2.name == 'Datasets'
    assert cat2.url == 'http://www.esrl.noaa.gov/thredds/catalog/Datasets/catalog.xml'


# def test_utas_tpac():
#     cat = read_url('http://portal.sf.utas.edu.au/thredds/catalog.xml')
#     assert cat.name == 'TPAC Digital Library Data Server Catalog'
#     assert cat.url == 'http://portal.sf.utas.edu.au/thredds/catalog.xml'


# def test_utas_tpac_html():
#     cat = read_url('http://portal.sf.utas.edu.au/thredds/catalog.html')
#     assert cat.name == 'TPAC Digital Library Data Server Catalog'
#     assert cat.url == 'http://portal.sf.utas.edu.au/thredds/catalog.xml'
