from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='drone_1_manager',     # Replace with your real package
            executable='mission_handler_node',  # Replace with your actual node
            name='mission_handler_node',
            output='screen'
        ),
        Node(
            package='drone_1_manager',       # Replace with your real package
            executable='status_publisher_node',       # Replace with your actual node
            name='status_publisher_node',
            output='screen'
        ),
        Node(
            package='drone_1_manager',       # Replace with your real package
            executable='offboard_controller_node',       # Replace with your actual node
            name='offboard_controller_node',
            output='screen'
        ),
        Node(
            package='drone_2_manager',       # Replace with your real package
            executable='status_publisher_node',       # Replace with your actual node
            name='status_publisher_node',
            output='screen'
        )
    ])
