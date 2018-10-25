#!/usr/bin/env python

from setuptools import setup

package_name = 'qt_gui'

setup(
    packages=['qt_gui'],
    package_dir={'': 'qt_gui'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
)
