from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Path to this file's directory
    launch_file_dir = os.path.dirname(os.path.realpath(__file__))

    # PX4 dir is beside gcs_ws
    px4_path = os.path.realpath(os.path.join(launch_file_dir, '../../../PX4-Autopilot'))

    # ROS 2 workspace setup file
    ros2_ws_setup = os.path.realpath(os.path.join(launch_file_dir, '../../../install/setup.bash'))

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gnome-terminal',

                # PX4 
                '--tab', '-t', 'PX4 SIMULATION', '--',
                'bash', '-c', f'cd {px4_path} && ./Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m iris -n 2; exec bash',

                # XRCE Agent 
                '--tab', '-t', 'DDS', '--',
                'bash', '-c', 'sleep 5 && MicroXRCEAgent udp4 -p 8888; exec bash',

                # XRCE Agent 2
                '--tab', '-t', 'Downloads', '--',
                'bash', '-c', 'cd && ./Downloads/QGroundControl.AppImage; exec bash',

                # drones Launch 
                '--tab', '-t', 'ROS2 Launch 1', '--',
                'bash', '-c', f'sleep 20 && source {ros2_ws_setup} && ros2 launch drone_launch drone.launch.py; exec bash',

                # GCS Launch 
                '--tab', '-t', 'ROS2 Launch 2', '--',
                'bash', '-c', f'sleep 25 && source {ros2_ws_setup} && ros2 launch gcs_controller gcs.launch.py; exec bash',
            ],
            shell=False
        )
    ])
