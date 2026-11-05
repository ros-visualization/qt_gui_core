from setuptools import setup

package_name = 'qt_gui_app'

setup(
    name=package_name,
    version='3.0.4',
    packages=[],
    scripts=['scripts/' + package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dirk Thomas',
    maintainer='Dirk Thomas',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'qt_gui_app provides the main to start an instance of the integrated graphical user '
        'interface provided by qt_gui.'
    ),
    license='BSD',
    extras_require={
        'test': [
            'pytest',
        ],
    },
)
