from setuptools import setup

package_name = 'qt_dotgraph'

setup(
    name=package_name,
    version='2.8.3',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Thibault Kruse',
    maintainer='Chris Lalancette',
    maintainer_email='clalancette@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'qt_dotgraph provides helpers to work with dot graphs.'
    ),
    license='BSD',
    tests_require=['pytest'],
)
