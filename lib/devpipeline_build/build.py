#!/usr/bin/python3
"""This module initiates the build."""

import argparse

import devpipeline_core.command
import devpipeline_configure.load

import devpipeline_build.builder
import devpipeline_build.version


def _configure(parser):
    devpipeline_core.command.setup_task_parser(parser)
    devpipeline_core.command.add_version_info(parser, devpipeline_build.version.STRING)


def _execute(arguments):
    devpipeline_core.command.process_tasks(
        arguments,
        [devpipeline_build.builder.BUILD_TASK],
        devpipeline_configure.load.update_cache,
    )


_BUILD_COMMAND = ("Build and install a set of components.", _configure, _execute)
