#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['package_dir'] = {}
d['scripts'] = ['bin/qt_gui_app']

setup(**d)
