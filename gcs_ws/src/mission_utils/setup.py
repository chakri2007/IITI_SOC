from setuptools import find_packages, setup

package_name = 'mission_utils'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
<<<<<<< HEAD
=======
            'waypoints_dataset = mission_utils.waypoints_dataset:main',
            'geotags_dataset = mission_utils.geotags_dataset:main',
            'geotags_visited_updater = mission_utils.geotags_visited_updater:main',
>>>>>>> dual_drone
        ],
    },
)
