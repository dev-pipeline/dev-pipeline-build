#!/usr/bin/python3
"""This module initiates the build."""

import argparse

import devpipeline_core.command
import devpipeline_configure.load

import devpipeline_build.builder


def _list_builders():
    for builder in sorted(devpipeline_build.BUILDERS):
        print("{} - {}".format(builder, devpipeline_build.BUILDERS[builder][1]))


_MAJOR = 0
_MINOR = 5
_PATCH = 0

_STRING = "{}.{}.{}".format(_MAJOR, _MINOR, _PATCH)


class BuildCommand(devpipeline_core.command.TaskCommand):
    """Class to provide build functionality to dev-pipeline."""

    def __init__(self, config_fn):
        super().__init__(
            config_fn=config_fn,
            tasks=[devpipeline_build.builder.BUILD_TASK],
            prog="dev-pipeline build",
            description="Build targets",
        )
        self.add_argument(
            "--list-builders",
            action="store_true",
            default=argparse.SUPPRESS,
            help="List the available builder tools",
        )
        self.set_version(_STRING)

    def process(self, arguments):
        if "list_builders" in arguments:
            _list_builders()
        else:
            super().process(arguments)


def main(args=None, config_fn=devpipeline_configure.load.update_cache):
    # pylint: disable=missing-docstring
    builder = BuildCommand(config_fn)
    # pylint: disable=missing-docstring
    devpipeline_core.command.execute_command(builder, args)


_BUILD_COMMAND = (main, "Build and install a set of components.")

if __name__ == "__main__":
    main()
