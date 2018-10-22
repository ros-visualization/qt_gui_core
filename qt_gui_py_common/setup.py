#!/usr/bin/env python

from setuptools import setup

d = dict(
    packages=['qt_gui_py_common'],
    package_dir={'': 'python_qt_binding'}
)

setup(**d)
