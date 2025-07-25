from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..','..', '..'))
    mission_path = os.path.join(base_path, 'mission_files')

    kml_file_path = os.path.join(mission_path, 'iit_survey.kml')
    waypoint_file_path = os.path.join(mission_path, 'iiti_waypoints.json')
    geotag_file_path = os.path.join(mission_path, 'geotags.json')
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
            output='screen',
            parameters=[
                {'geotag_file_path': geotag_file_path},
                ]
        ),
        Node(
            package='gcs_controller',
            executable='waypoint_manager_node',
            name='waypoint_manager_node',
            output='screen',
            parameters=[
                {'json_file_path': waypoint_file_path},
                {'batch_size': 5}
            ]
        ),
        Node(
            package='mission_utils',
            executable='waypoints_dataset',
            name='waypoints_dataset',
            output='screen',
            parameters=[{
                'waypoint_file_path': waypoint_file_path
            }]
        ),
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
    ])
