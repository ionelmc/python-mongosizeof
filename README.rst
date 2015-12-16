========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-mongosizeof/badge/?style=flat
    :target: https://readthedocs.org/projects/python-mongosizeof
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-mongosizeof.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-mongosizeof

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-mongosizeof?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-mongosizeof

.. |requires| image:: https://requires.io/github/ionelmc/python-mongosizeof/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-mongosizeof/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/ionelmc/python-mongosizeof/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-mongosizeof

.. |version| image:: https://img.shields.io/pypi/v/mongosizeof.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/mongosizeof

.. |downloads| image:: https://img.shields.io/pypi/dm/mongosizeof.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/mongosizeof

.. |wheel| image:: https://img.shields.io/pypi/wheel/mongosizeof.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/mongosizeof

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/mongosizeof.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/mongosizeof

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/mongosizeof.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/mongosizeof


.. end-badges

A fast (and possibly inaccurate) estimator of amount of memory python objects would take in a mongodb collection.

* Free software: BSD license

Installation
============

::

    pip install mongosizeof

Documentation
=============

https://python-mongosizeof.readthedocs.org/

Development
===========

To run the all tests run::

    tox
