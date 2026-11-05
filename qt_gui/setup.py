from setuptools import setup

package_name = 'qt_gui'

setup(
    name=package_name,
    version='3.0.4',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
            ['resource/dock_widget_title_bar.ui',
             'resource/perspective_create.ui',
             'resource/ros_org_vertical.png']),
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
        'qt_gui provides the infrastructure for an integrated graphical user interface based '
        'on Qt.'
    ),
    license='BSD',
    extras_require={
        'test': [
            'pytest',
        ],
    },
)
