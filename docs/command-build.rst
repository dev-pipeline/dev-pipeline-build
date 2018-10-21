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
* :code:`build.tool` - (**Required**) The build tool to use.  Available options
  are a union of what's built in and options available through installed
  plugins.
* :code:`build.install_path` - The path *within the build directory* to install
  a package.  If unspecified, :code:`install` will be used.
* :code:`build.no_install` - Prevent a package from being installed.
* :code:`build.artifact_paths` - A comma-separated list of key value pairs of
  *installed* build artifacts to find.  After the build is completed, each
  requested file will be found and the full path of the owner will be stored in
  :code:`dp.build.artifact_path.<key>`.  For example,
  :code:`build.artifact_paths = cmake_path=fmt-targets.cmake` will store the
  location of :code:`fmt-targets.cmake` in
  :code:`dp.build.artifact_path.cmake_path`.  Because the artifacts can't be
  found until after being installed, be sure you've set the corresponding
  :code:`depends` appropriately.


Deprecated Options
------------------
* :code:`build` - Use :code:`build.tool`
* :code:`install_path` - Use :code:`build.install_path`
* :code:`no_install` - Use :code:`build.no_install`
