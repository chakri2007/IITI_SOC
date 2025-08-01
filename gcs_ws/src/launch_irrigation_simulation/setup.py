from setuptools import find_packages, setup

package_name = 'launch_irrigation_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/dual_drone_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='burrachakrapani',
    maintainer_email='burrachakrapani@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
