from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gcs_controller',
            executable='swarm_supervisor_node',
            name='swarm_supervisor_node',
            output='screen'
        ),
        Node(
            package='gcs_controller',
            executable='geotag_manager_node',
            name='geotag_manager_node',
            output='screen'
        ),
        Node(
            package='gcs_controller',
            executable='waypoint_manager_node',
            name='waypoint_manager_node',
            output='screen'
        )
    ])
