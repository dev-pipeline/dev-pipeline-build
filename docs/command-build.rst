build
=====

Synopsis
--------
::

    dev-pipeline build [-h] [--list-builders] [--dependencies DEPENDENCIES]
                       [--executor EXECUTOR]
                       [targets [targets ...]]


Description
-----------
This tool builds one or more components along with their dependencies
(controlled by :code:`--dependencies`).  The specific order components are
built isn't guaranteed, even across sequential runs.

If no targets are specified, all targets will be built.


Options
-------
  -h, --help            show this help message and exit
  --list-builders       List the available builder tools
  --dependencies DEPENDENCIES
                        Control how build dependencies are handled. (default:
                        deep)
  --executor EXECUTOR   The method to execute commands. (default: quiet)


Config Options
--------------
* :code:`build` - (**Required**) The build tool to use.  Available options are
  a union of what's built in and options available through installed plugins.
* :code:`install_path` - The path *within the build directory* to install a
  package.  If unspecified, :code:`install` will be used.
* :code:`no_install` - Prevent a package from being installed.
