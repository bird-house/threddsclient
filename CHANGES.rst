=======
Changes
=======

Unreleased
==================

* add missing classifiers and python requirements to ``setup.py`` to allow validators to detect appropriate versions
* add python 3.9, 3.10 and 3.11 to the supported versions in ``setup.py`` and validate them in GitHub CI
* drop Travis CI configuration in favor of GitHub CI
* fix ``test_noaa`` with the target THREDDS server responding differently than originally tested

0.4.3 (2023-05-31)
==================

* fix xml parsing for recent versions

0.4.2 (2019-11-20)
==================

* fixed conda links in Readme.

0.4.1 (2019-11-06)
==================

* fixed docs formatting.

0.4.0 (2019-11-06)
==================

* drop Python 2.7 (#5)
* fix pip install (#4)

0.3.5 (2018-10-05)
==================

* support for Python 3.x (#1)

0.3.4 (2015-10-25)
==================

* fixed travis build/tests
* updated docs

0.3.3 (2015-10-24)
==================

* converted docs to rst.
* MANIFEST.in added.

0.3.2 (2015-07-15)
==================

*  append catalog.xml to catalog url if missing
*  crawl method added

0.3.1 (2015-06-14)
==================

*  fixed catalog.follow()
*  using dataset.download_url()
*  added ipython example
*  cleaned up Readme

0.3.0 (2015-06-13)
==================

*  Refactored
*  added catalog.opendap_urls()

0.2.0 (2015-06-08)
==================

*  Refactored
*  using CollectionDataset
*  added catalog.download_urls()

0.1.1 (2015-06-05)
==================

*  Fixed catalog generation.
*  added pytest dependency.

0.1.0 (2015-03-13)
==================

*  Version by https://github.com/ScottWales/threddsclient.
