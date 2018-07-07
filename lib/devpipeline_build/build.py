#!/usr/bin/python3
"""This module initiates the build."""

import devpipeline_core.command

import devpipeline_build.build


def main(args=None):
    # pylint: disable=missing-docstring
    builder = devpipeline_core.command.make_command([
        devpipeline_build.builder.build_task
    ], prog="dev-pipeline build", description="Build targets")
    devpipeline_core.command.execute_command(builder, args)

_BUILD_COMMAND = (main, "Build and install a set of components.")

if __name__ == '__main__':
    main()
