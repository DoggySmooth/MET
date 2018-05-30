#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    scripts=[
        'met/scripts/met-x2j.py', 'met/scripts/met-graph.py',
        'met/scripts/met-report.py', 'met/scripts/xmlMerger.py',
        'met/scripts/compile.py'
    ])
