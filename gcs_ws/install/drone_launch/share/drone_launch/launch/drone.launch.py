from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='drone_1_manager',     
            executable='mission_handler_node',  
            name='mission_handler_node',
            output='screen'
        ),
        Node(
            package='drone_1_manager',      
            executable='status_publisher_node',       
            output='screen'
        ),
        Node(
            package='drone_1_manager',       
            executable='offboard_controller_node',       
            name='offboard_controller_node',
            output='screen'
        ),
        Node(
            package='drone_1_manager',    
            executable='geotagging_node',  
            name='geotagging_node',
            output='screen'
        ),
         Node(
            package='drone_2_manager',     
            executable='mission_handler_node', 
            name='mission_handler_node',
            output='screen'
        ),
        Node(
            package='drone_2_manager',       
            executable='status_publisher_node',   
            name='status_publisher_node',
            output='screen'
        ),
        Node(
            package='drone_2_manager',      
            executable='offboard_controller_node',       
            name='offboard_controller_node',
            output='screen'
        ),
        Node(
            package='drone_2_manager',     
            executable='geotagging_node', 
            name='geotagging_node',
            output='screen'
        ),
    ])
