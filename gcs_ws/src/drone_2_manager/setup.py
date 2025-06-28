from setuptools import find_packages, setup

package_name = 'drone_2_manager'

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
            'mission_handler_node = drone_1_manager.mission_handler_node:main',
            'status_publisher_node = drone_1_manager.status_publisher_node:main',
=======
            'mission_handler_node = drone_2_manager.mission_handler_node:main',
            'status_publisher_node = drone_2_manager.status_publisher_node:main',
            'offboard_controller_node = drone_2_manager.offboard_controller_node:main',
            'geotagging_node = drone_2_manager.geotagging_node:main',
>>>>>>> dual_drone
        ],
    },
)
