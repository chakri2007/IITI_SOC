# Coordinated Dual Drone Framework for Coverage Based Irrigation Tasks

### Team Members

_**Team Member 1**:  [@Chakrapani](https://github.com/chakri2007)_  
_**Team Member 2**:  [@BhavMakhija](https://github.com/Bhavdex)_  
_**Team Member 3**:  [@Tejasri](https://github.com/Tejasri676)_

### Mentors

_**Mentor 1**:  [@sibasish](https://github.com/sibasish)_  
_**Mentor 2**:  [@pohrselvan](https://github.com/pohrselvan)_

---

# Introduction

This project presents a dual-drone simulation framework for autonomous coverage and irrigation tasks in agricultural fields. Using ROS 2 and PX4 in a Gazebo environment, both drones are designed to collaboratively perform geotagging and irrigation based on predefined severity scores. The drones monitor their own battery and water levels, and dynamically return to the base station for recharging or refilling as needed. A shared coordination and queue-based logic allows seamless task handovers and ensures minimal downtime. By implementing intelligent task allocation, role switching, and time-efficiency strategies, the system minimizes total mission duration while maintaining full coverage and effective irrigation. The framework demonstrates how coordinated swarm behavior between just two drones can significantly improve operational efficiency in precision agriculture applications.

---

#  Simulation Demo

Click the link below to watch a demo video of the full simulation workflow:

▶ **[Watch Demo on Google Drive](https://drive.google.com/file/d/19WJvJXVDr51PRfOCrWdp88heIVSyclve/view?usp=sharing)**

---

# Technology Stack

The project uses the following software stack and tools:

- **Operating System**: Ubuntu 22.04 (Jammy Jellyfish)  
- **Robotics Framework**: ROS 2 Humble Hawksbill  
- **Autopilot Firmware**: PX4 v1.15.4  
- **Simulation Engine**: Gazebo Classic  
- **Middleware Communication**: Micro XRCE-DDS  
- **Build System**: colcon  
- **Mapping Library**: pyproj (Python)

---

# Installation Dependencies

Before running the simulation, ensure the following dependencies are installed:

## PX4 Messages (version 15.4)
```bash
git clone -b release/1.15 https://github.com/PX4/px4_msgs.git
cd px4_msgs
colcon build --packages-select px4_msgs
source install/setup.bash
```

## Python Dependencies
Install `pyproj`:
```bash
pip install pyproj
```

---

# Command Sequence for Irrigation Simulation

The following terminal commands are required to run the full dual-drone simulation for coverage-based irrigation. These steps assume that all prior setup (PX4 SITL, ROS 2 environment, workspace build, dependencies, and Micro XRCE-DDS installation) has been fully completed.

## 1. Launch PX4 SITL
```bash
./Tools/simulation/gazebo-classic/sitl_multiple_run.sh -m iris -n 2
```

## 2. Start Micro XRCE-DDS Agent
```bash
MicroXRCEAgent udp4 -p 8888
```

## 3. Source the ROS 2 workspace
```bash
source install/setup.bash
```

## 4. Launch Dual Drone Stack
```bash
ros2 launch drone_launch drone.launch.py
```

## 5. Launch Ground Control Station (GCS)
```bash
ros2 launch gcs_controller gcs.launch.py
```

---

# Additional Notes

- Start **QGroundControl (QGC)** to visualize the real-time drone path tracing and geotagging progress.

- Alternatively, a **single launch file** can be used to run the complete simulation:
```bash
ros2 run launch_irrigaiton_simulation dual_drone_launch.py
```
>  **Note**: This launch file may require modifications to match your local system's file paths and workspace structure.
