from setuptools import setup

package_name = 'qt_gui_py_common'

setup(
    name=package_name,
    version='3.0.4',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
            ['resource/simple_settings_dialog.ui']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dorian Scholz',
    maintainer='Dorian Scholz',
    maintainer_email='scholz@sim.tu-darmstadt.de',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'qt_gui_py_common provides common functionality for GUI plugins written in Python.'
    ),
    license='BSD',
    extras_require={
        'test': [
            'pytest',
        ],
    },
)
