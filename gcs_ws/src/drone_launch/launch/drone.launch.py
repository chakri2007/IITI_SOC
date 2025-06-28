from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
<<<<<<< HEAD
            package='drone_1_manager',     # Replace with your real package
            executable='mission_handler_node',  # Replace with your actual node
=======
            package='drone_1_manager',     
            executable='mission_handler_node',  
>>>>>>> dual_drone
            name='mission_handler_node',
            output='screen'
        ),
        Node(
<<<<<<< HEAD
            package='drone_1_manager',       # Replace with your real package
            executable='status_publisher_node',       # Replace with your actual node
=======
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
>>>>>>> dual_drone
            name='status_publisher_node',
            output='screen'
        ),
        Node(
<<<<<<< HEAD
            package='drone_2_manager',       # Replace with your real package
            executable='status_publisher_node',       # Replace with your actual node
            name='status_publisher_node',
            output='screen'
        )
=======
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
>>>>>>> dual_drone
    ])
