=========================
Thredds Client for Python
=========================

|Travis Build| |Install with Conda| |Join the Chat|

Installing Thredds Client
=========================

Anaconda
--------

|Version-GitHub| |Version-Anaconda| |Version-PyPI| |Downloads|

Thredds client is available as Anaconda package. Install it with the
following command:

.. code-block:: bash

    conda install -c conda-forge threddsclient

From PyPI
---------

Thredds Client is available from PyPI to install directly with ``pip`` or ``poetry``.

.. code-block:: bash

    pip install threddsclient


.. code-block:: bash

    poetry add threddsclient


From GitHub
-----------

Check out code from the birdy GitHub repo and start the installation:

.. code-block:: bash

    git clone https://github.com/bird-house/threddsclient.git
    cd threddsclient
    conda env create -f environment.yml
    source activate threddsclient
    python setup.py develop

Alternatively, you can also install it directly with ``pip`` using a virtual environment of your choice:

.. code-block:: bash

    pip install "threddsclient @ git+https://github.com/bird-house/threddsclient.git"


Using Thredds Client
====================

Read the Thredds tutorial on catalogs: `Thredds Catalog
Primer <http://www.unidata.ucar.edu/software/thredds/current/tds/tutorial/CatalogPrimer.html>`__

Get download URLs of a catalog
------------------------------

.. code-block:: python

        import threddsclient
        urls = threddsclient.download_urls('http://example.com/thredds/catalog.xml')

Get OpenDAP URLs of a catalog
-----------------------------

.. code-block:: python

        import threddsclient
        urls = threddsclient.opendap_urls('http://example.com/thredds/catalog.xml')

Navigate in catalog
-------------------

Start reading a catalog

.. code-block:: python

        import threddsclient
        cat = threddsclient.read_url('http://example.com/thredds/catalog.xml')

Get a list of references to other catalogs & follow them

.. code-block:: python

        refs = cat.references

        print refs[0].name
        cat2 = refs[0].follow()

Get a list of datasets in this catalog

.. code-block:: python

        data  = cat.datasets

Get flat list of all direct datasets (data files) in the catalog

.. code-block:: python

        datasets = cat.flat_datasets()

Get flat list of all references in the catalog

.. code-block:: python

        references = cat.flat_references()

Crawl thredds catalog
---------------------

Crawl recursive all direct datasets in catalog following the catalog
references. Stop recursion at a given depth level.

.. code-block:: python

       import threddsclient
       for ds in threddsclient.crawl('http://example.com/thredds/catalog.xml', depth=2):
           print ds.name

Development
===========

Install sources
---------------

Check out code from the birdy GitHub repo and start the installation:

.. code-block:: sh

   git clone https://github.com/bird-house/threddsclient.git
   cd threddsclient
   conda env create -f environment.yml
   python setup.py develop

Install additional dependencies:

.. code-block:: sh

    conda install pytest flake8 sphinx bumpversion
    # OR
    pip install -r requirements_dev.txt

Bump a new version
------------------

Make a new version of Birdy in the following steps:

* Make sure everything is commit to GitHub.
* Update ``CHANGES.rst`` with the next version.
* Dry Run: ``bumpversion --dry-run --verbose --new-version {NEW_VERSION} patch``
* Do it: ``bumpversion --new-version {NEW_VERSION} patch``
* Push it: ``git push --tags``

See the bumpversion_ documentation for details.

.. _bumpversion: https://pypi.org/project/bumpversion/

Examples with IPython Notebook
------------------------------

-  `NOAA Thredds
   Catalog <http://nbviewer.ipython.org/github/bird-house/threddsclient/blob/master/examples/noaa_example.ipynb>`__

.. |Travis Build| image:: https://travis-ci.org/bird-house/threddsclient.svg?branch=master
   :target: https://travis-ci.org/bird-house/threddsclient
.. |Install with Conda| image:: https://anaconda.org/conda-forge/threddsclient/badges/installer/conda.svg
   :target: https://anaconda.org/conda-forge/threddsclient
.. |License| image:: https://anaconda.org/conda-forge/threddsclient/badges/license.svg
   :target: https://anaconda.org/conda-forge/threddsclient
.. |Join the Chat| image:: https://badges.gitter.im/bird-house/birdhouse.svg
   :target: https://gitter.im/bird-house/birdhouse?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Version-GitHub| image:: https://img.shields.io/github/v/release/bird-house/threddsclient?label=GitHub
   :target: https://github.com/bird-house/threddsclient/releases
.. |Version-Anaconda| image:: https://anaconda.org/conda-forge/threddsclient/badges/version.svg
   :target: https://anaconda.org/conda-forge/threddsclient
.. |Version-PyPI| image:: https://img.shields.io/pypi/v/threddsclient?color=blue
   :target: https://pypi.org/project/threddsclient/
.. |Downloads| image:: https://anaconda.org/conda-forge/threddsclient/badges/downloads.svg
   :target: https://anaconda.org/conda-forge/threddsclient
