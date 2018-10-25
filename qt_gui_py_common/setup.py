#!/usr/bin/env python

from setuptools import setup
package_name = 'qt_gui_py'

setup(
    packages=['qt_gui_py_common'],
    package_dir={'': 'python_qt_binding'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/ament_index/resource_index/ui_files', ['resource/simple_settings_dialog.ui', ]),
        ('share/' + package_name, ['package.xml']),
    ],
)
