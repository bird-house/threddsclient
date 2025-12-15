=======
Changes
=======

`Unreleased <https://github.com/bird-house/threddsclient/tree/master>`_
==========================================================================================

* Nothing new for the moment.

.. _changes_0.4.7:

`0.4.7 <https://github.com/bird-house/threddsclient/tree/v0.4.7>`_ (2025-12-15)
==========================================================================================

* Add `url` and `download_url` to project setup for reference by PyPI package.
* Add Python 3.13 and 3.14 to CI and project.
* Update default Python 3.13 in CI for tests.
* Remove Python 3.6 and 3.7 from CI.

.. _changes_0.4.6:

`0.4.6 <https://github.com/bird-house/threddsclient/tree/v0.4.6>`_ (2024-07-09)
==========================================================================================

* Drop Python 3.7.
* Add Python 3.12.

.. _changes_0.4.5:

`0.4.5 <https://github.com/bird-house/threddsclient/tree/v0.4.5>`_ (2024-01-22)
==========================================================================================

* Fixed TDS v5 and HYRAX catalog traversing issue (#15)

.. _changes_0.4.4:

`0.4.4 <https://github.com/bird-house/threddsclient/tree/v0.4.4>`_ (2023-07-11)
==========================================================================================

* add shield badges for PyPI and GitHub releases
* fix rendering of code blocks in ``README.rst``
* add missing classifiers and python requirements to ``setup.py`` to allow validators to detect appropriate versions
* add python 3.9, 3.10 and 3.11 to the supported versions in ``setup.py`` and validate them in GitHub CI
* drop Travis CI configuration in favor of GitHub CI
* fix ``test_noaa`` with the target THREDDS server responding differently than originally tested

`0.4.3 <https://github.com/bird-house/threddsclient/tree/v0.4.3>`_ (2023-05-31)
==========================================================================================

* fix xml parsing for recent versions

`0.4.2 <https://github.com/bird-house/threddsclient/tree/v0.4.2>`_ (2019-11-20)
==========================================================================================

* fixed conda links in Readme.

`0.4.1 <https://github.com/bird-house/threddsclient/tree/v0.4.1>`_ (2019-11-06)
==========================================================================================

* fixed docs formatting.

`0.4.0 <https://github.com/bird-house/threddsclient/tree/v0.4.0>`_ (2019-11-06)
==========================================================================================

* drop Python 2.7 (#5)
* fix pip install (#4)

`0.3.5 <https://github.com/bird-house/threddsclient/tree/v0.3.5>`_ (2018-10-05)
==========================================================================================

* support for Python 3.x (#1)

`0.3.4 <https://github.com/bird-house/threddsclient/tree/v0.3.4>`_ (2015-10-25)
==========================================================================================

* fixed travis build/tests
* updated docs

0.3.3 (2015-10-24)
==========================================================================================

* converted docs to rst.
* MANIFEST.in added.

0.3.2 (2015-07-15)
==========================================================================================

*  append catalog.xml to catalog url if missing
*  crawl method added

0.3.1 (2015-06-14)
==========================================================================================

*  fixed catalog.follow()
*  using dataset.download_url()
*  added ipython example
*  cleaned up Readme

0.3.0 (2015-06-13)
==========================================================================================

*  Refactored
*  added catalog.opendap_urls()

0.2.0 (2015-06-08)
==========================================================================================

*  Refactored
*  using CollectionDataset
*  added catalog.download_urls()

0.1.1 (2015-06-05)
==========================================================================================

*  Fixed catalog generation.
*  added pytest dependency.

0.1.0 (2015-03-13)
==========================================================================================

*  Version by https://github.com/ScottWales/threddsclient.
