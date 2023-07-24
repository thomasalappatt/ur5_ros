


~/catkin_ws/src$ git clone  https://github.com/ros-industrial/universal_robot.git $
$ rosdep update
$ rosdep install --rosdistro $ROS_DISTRO --ignore-src --from-paths src

Then build your workspace:

~/catkin_ws$ catkin_make
$ source $HOME/catkin_ws/devel/setup.bash

For the first task

run 

roslaunch ur5_gazebo task1.launch

The amplitude values in this launch file are the joint angle in radians 
Default values are given . Please change if required 







