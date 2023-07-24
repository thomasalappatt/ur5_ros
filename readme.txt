nstall Gazebo if needed:

$ curl -sSL http://get.gazebosim.org | sh

If not already done from the previous tutorials please install the universal_robot package:

~/catkin_ws/src$ git clone -b <distro>-devel https://github.com/ros-industrial/universal_robot.git $
$ rosdep update
$ rosdep install --rosdistro $ROS_DISTRO --ignore-src --from-paths src

Then build your workspace:

~/catkin_ws/src$ cd ..
~/catkin_ws$ catkin_make
$ source $HOME/catkin_ws/devel/setup.bash

Now copy the content of the URDF for Gazebo to your local file system into a file named ur5_gazebo.urdf. Then run the following two commands to spawn the robot in Gazebo:

$ roslaunch gazebo_ros empty_world.launch
$ rosrun gazebo_ros spawn_model -file <path-to-your-gazebo-urdf/ur5_.urdf -urdf -x 0 -y 0 -z 0.1 -model ur5

Alternatively, you could simply start the simulation with a launch file from the ur5_gazebo package which also launches a controller:

$ roslaunch ur_gazebo ur5.launch






