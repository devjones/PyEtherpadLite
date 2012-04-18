#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
setup(
    name='pyetherpadlite',
    version='0.1',
    description='Python bindings for Etherpad-Lite\'s HTTP API. (https://github.com/Pita/etherpad-lite)',
    author='devjones',
    url='https://github.com/devjones/PyEtherpadLite',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

