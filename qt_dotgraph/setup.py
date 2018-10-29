#!/usr/bin/env python

from distutils.core import setup

from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['qt_dotgraph'],
    package_dir={'': 'qt_dotgraph'}
)

setup(**d)
