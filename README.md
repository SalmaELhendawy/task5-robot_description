## 1. Project Overview
This project provides a complete ROS 2 package (robot_description) for modeling and simulating a custom differential-drive mobile robot. It integrates custom **CAD meshes** (ZED camera and LiDAR), configures **Gazebo Sim** simulation with sensor plugins (Diff Drive, GPU LiDAR, and RGB Camera), and sets up **ros_gz_bridge** 
for seamless communication between ROS 2 and Gazebo.
---------------------------------------------------------------------------------------------------------------
## 2. Package Structure
task5-robot_description/
└── robot_description/
    ├── urdf/
    │   ├── robot.urdf.xacro
    │   └── robot.gazebo.xacro
    ├── meshes/
    │   ├── lidar.STL
    │   └── zed.stl
    ├── config/
    │   └── gz_bridge.yaml
    ├── launch/
    │   ├── display.launch.py
    │   └── gazebo.launch.py
    ├── rviz/
    │   └── robot_view.rviz
    ├── package.xml
    ├── CMakeLists.txt
    └── README.md
    -----------------------------------------------------------------------------------------------------------------------------------------
    ## 3. Linux Commands Used and ROS command Used
   ```
    mkdir -p ~/workspaces/my_robot_ws/src
    cd ~/workspaces/my_robot_ws
    echo "source ~/workspaces/my_robot_ws/install/setup.bash" >> ~/.bashrc
   -----------------------------------------------
    Workspace Building:
    colcon build --packages-select robot_description
    ------------------------------------------
    Node & Launch Execution:
    ros2 launch robot_description display.launch.py
    ros2 launch robot_description gazebo.launch.py
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
    -----------------------------------------------------
    Diagnostics:
    ros2 topic list
    ros2 topic echo /scan
    ros2 run tf2_tools view_frames
   ```
---------------------------------------------------------------------------------------------------------------------------------------------
## 4. How to Launch RViz
```
write rviz2 in terminal 
```
---------------------------------------------------------------------------------------------------------------------
## 5. How to Launch Gazebo
```
ros2 launch robot_description display.launch.py
ros2 launch robot_description gazebo.launch.py
```
------------------------------------------------------------------------------------------------------------------------------------------

## 6. Expected Topics
/cmd_vel (geometry_msgs/msg/Twist) : Robot movement control commands.

/odom (nav_msgs/msg/Odometry) : Odometry data published by Gazebo.

/scan (sensor_msgs/msg/LaserScan) : 2D LiDAR point measurements.

/camera/image_raw (sensor_msgs/msg/Image) :Raw RGB camera feed.

/tf & /tf_static (tf2_msgs/msg/TFMessage) : Coordinate frame transformations.
------------------------------------------------------------------------------------------------------------------------------
## 7. How to Move the Robot
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

--------------------------------------------------------------------------------------------------------------------------------
## 8.TF Tree Explanation

odom to base_footprint: Tracks robot movement and odometry in the environment.

base_footprint to base_link: Connects ground projection to the chassis center.

base_link to left_wheel_link and right_wheel_link: Sets wheel mounting points and rotation axes.

base_link to lidar_link and camera_link: Defines sensor physical mounting positions.

camera_link to camera_optical_link: Rotates frame to match ROS optical standards.


  -----------------------------------------------------------------------------------------------------------------------------
  ## 9.Screenshots

  1-Robot in RViz:
  <img width="455" height="320" alt="robot in rviz" src="https://github.com/user-attachments/assets/8d3ece0b-7773-4241-ac13-87726e9ce1ac" />

 2- Robot in Gazebo:
 <img width="1910" height="1063" alt="robot in Gazebo" src="https://github.com/user-attachments/assets/5ae6a017-559c-4d39-ad8e-a70aa58e66de" />

 3- Lidar Visualization:
 <img width="1919" height="994" alt="lidar visualization" src="https://github.com/user-attachments/assets/cc84e1ab-6263-46b4-a595-6aa9c3801da5" />

 4- camera visualization
 <img width="182" height="125" alt="cam1" src="https://github.com/user-attachments/assets/b591f611-1eb1-4c32-adfd-b99219f71e9a" />
 <img width="791" height="287" alt="camera visualization" src="https://github.com/user-attachments/assets/26b739b8-f25b-4d65-bdf3-997d0d3fd228" />




