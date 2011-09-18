#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
 
setup(
    name='PyEtherpadLite',
    version='0.1',
    description='Python bindings for Etherpad-Lite\'s HTTP API. (https://github.com/Pita/etherpad-lite)',
    author='devjones',
    url='https://github.com/devjones/PyEtherpadLite',
    package_dir={'': 'src'},
    py_modules=[
        'PyEtherpadLite',
    ],
)

