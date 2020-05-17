#!/usr/bin/python3
"""This module initiates the build."""

import argparse

import devpipeline_core.command
import devpipeline_configure.load

import devpipeline_build.builder


_MAJOR = 0
_MINOR = 5
_PATCH = 0

_STRING = "{}.{}.{}".format(_MAJOR, _MINOR, _PATCH)


def _configure(parser):
    # parser.add_argument(
    # "--list-builders",
    # action="store_true",
    # default=argparse.SUPPRESS,
    # help="List the available builder tools",
    # )
    devpipeline_core.command.setup_task_parser(parser)
    devpipeline_core.command.add_version_info(parser, _STRING)


def _execute(arguments):
    def _list_builders():
        for builder in sorted(devpipeline_build.BUILDERS):
            print("{} - {}".format(builder, devpipeline_build.BUILDERS[builder][1]))

    if "list_builders" in arguments:
        _list_builders()
    else:
        devpipeline_core.command.process_tasks(
            arguments,
            [devpipeline_build.builder.BUILD_TASK],
            devpipeline_configure.load.update_cache,
        )


_BUILD_COMMAND = ("Build and install a set of components.", _configure, _execute)
