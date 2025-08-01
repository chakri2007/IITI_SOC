from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction
import os

def generate_launch_description():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..','..', '..'))
    mission_path = os.path.join(base_path, 'mission_files')

    kml_file_path = os.path.join(mission_path, 'iit_survey.kml')
    waypoint_file_path = os.path.join(mission_path, 'iiti_waypoints.json')
    geotag_file_path = os.path.join(mission_path, 'geotags.json')

    return LaunchDescription([
        Node(
            package='mission_utils',
            executable='lawnmower_generator_node',
            name='lawnmower_generator_node',
            output='screen',
            parameters=[
                {'kml_file_path': kml_file_path},
                {'output_file': waypoint_file_path},
                {'spacing': 5.0},
                {'turnaround': 3.0},
                {'start_from': 'top'},
                {'altitude': 640.0}
            ]
        ),
        TimerAction(
            period=10.0,
            actions=[
                Node(
                    package='gcs_controller',
                    executable='geotag_manager_node',
                    name='geotag_manager_node',
                    output='screen',
                    parameters=[
                        {'geotag_file_path': geotag_file_path},
                    ]
                )
            ]
        ) ,       

        Node(
            package='mission_utils',
            executable='geotags_dataset',
            name='geotags_dataset',
            output='screen',
            parameters=[
                {'geotag_file_path': geotag_file_path},
            ]
        ),

        Node(
            package='mission_utils',
            executable='geotags_visited_updater',
            name='geotags_visited_updater',
            output='screen',
            parameters=[
                {'geotag_file_path': geotag_file_path},
            ]
        ),

        Node(
            package='gcs_controller',
            executable='swarm_supervisor_node',
            name='swarm_supervisor_node',
            output='screen'
        ),

        # Delayed launch of waypoint_manager_node (10 seconds)
        TimerAction(
            period=10.0,
            actions=[
                Node(
                    package='gcs_controller',
                    executable='waypoint_manager_node',
                    name='waypoint_manager_node',
                    output='screen',
                    parameters=[
                        {'json_file_path': waypoint_file_path},
                        {'batch_size': 5}
                    ]
                )
            ]
        ),

        Node(
            package='mission_utils',
            executable='waypoints_dataset',
            name='waypoints_dataset',
            output='screen',
            parameters=[
                {'waypoint_file_path': waypoint_file_path}
            ]
        ),
        Node(
            package='gcs_controller',
            executable='dynamic_role_swap_node',
            name='dynamic_role_swap_node',
            output='screen',
        ),
        Node(
            package='mission_utils',
            executable='surveillance_monitor_node',
            name='surveillance_monitor_node',
            output='screen',
            parameters=[
                {'waypoint_file_path': waypoint_file_path},
            ]
        ),
    ])