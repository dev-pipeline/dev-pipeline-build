dev-pipeline-build
==================
|codacy|
|code-climate|
|lgtm|
|lgtm-quality|

A `dev-pipeline`_ plugin to provide build functionality.  It will add the
:code:`build` command to :code:`dev-pipeline`, permitting use of any
installed builder plugin.


Installation
------------
The simplest way to install is using pip_.

.. code:: bash

    $ cd /path/to/dev-pipeline-build
    $ pip3 install

If you don't have pip available, you can run :code:`setup.py` directly.

.. code:: bash

    $ cd /path/to/dev-pipeline-build
    $ python3 setup.py install

You'll need scm plugins installed to do anything useful.


Documentation
-------------
Information about the :code:`build` command is avaialble in the
documentation_.


.. |codacy| image:: https://api.codacy.com/project/badge/Grade/f0ef1ab921d949dfb2884c7d7eefbbc1
    :target: https://www.codacy.com/app/snewell/dev-pipeline-build?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-pipeline/dev-pipeline-build&amp;utm_campaign=Badge_Grade
.. |code-climate| image:: https://api.codeclimate.com/v1/badges/942cba520cd3e1638653/maintainability
   :target: https://codeclimate.com/github/dev-pipeline/dev-pipeline-build/maintainability
   :alt: Maintainability
.. |lgtm| image:: https://img.shields.io/lgtm/alerts/g/dev-pipeline/dev-pipeline-build.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/dev-pipeline/dev-pipeline-build/alerts/
.. |lgtm-quality| image:: https://img.shields.io/lgtm/grade/python/g/dev-pipeline/dev-pipeline-build.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/dev-pipeline/dev-pipeline-build/context:python

.. _dev-pipeline: https://github.com/dev-pipeline/dev-pipeline
.. _documentation: docs/command-build.rst
.. _pip: https://pypi.python.org/pypi/pip
