# IITISoC-25-IVR009: Coordinated Dual Drone Framework for Coverage Based Irrigation Tasks

Team Members

_**Team Member 1**:  [@Chakrapani](https://github.com/chakri2007)_

_**Team Member 2**:  [@BhavMakhija](https://github.com/Bhavdex)_

_**Team Member 3**:  [@Tejasri](https://github.com/Tejasri676)_

Mentors

_**Mentor 1**:  [@sibasish](https://github.com/sibasish)_

_**Mentor 2**:  [@pohrselvan](https://github.com/pohrselvan)_

# Command Sequence for Irrigation Simulation

The following terminal commands are required to run the full dual-drone simulation for coverage-based irrigation. These steps assume that all prior setup (PX4 SITL, ROS 2 environment, workspace build, dependencies, and Micro XRCE-DDS installation) has been fully completed.

<pre><code>./Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m iris -n 2</code></pre>
This command launches the PX4 Software-In-The-Loop simulation in Gazebo Classic for the dual-drone environment.

<pre><code>MicroXRCEAgent udp4 -p 8888</code></pre>
This connects PX4 and ROS2 using the Micro XRCE-DDS Agent over UDP port 8888.

<pre><code>ros2 launch drone_launch drone.launch.py</code></pre>
This command launches the main control stack for both drones, including offboard control, mission handling, status publishing, geotagging, and drone recharge.

<pre><code>ros2 launch gcs_controller gcs.launch.py</code></pre>
This brings up the Ground Control Station logic, including the swarm supervisor, waypoint manager, and geotag manager to coordinate both drones.
