#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-build",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    install_requires=[
        'dev-pipeline-core >= 0.2.0'
    ],

    entry_points={
        'devpipeline.drivers': [
            'build = devpipeline_build.build:main'
        ],

        'devpipeline.builders': [
            'nothing = devpipeline_build.builder:_nothing_builder',
        ]
    },

    author="Stephen Newell",
    description="build tooling for dev-pipeline",
    license="BSD-2"
)
