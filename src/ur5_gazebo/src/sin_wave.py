#!/usr/bin/python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys
import math

def publish_sine_wave_positions(amplitudes, frequency):
    if len(amplitudes) != 6:
        raise ValueError("Please provide exactly 6 amplitude values for each joint.")
    
    rospy.init_node('sine_wave_position_publisher_node', anonymous=True)
    pub = rospy.Publisher('/eff_joint_traj_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        joint_traj_msg = JointTrajectory()
        joint_traj_msg.joint_names = ["elbow_joint", "shoulder_lift_joint", "shoulder_pan_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

        point = JointTrajectoryPoint()
        joint_positions = [amplitudes[i] * math.sin(2 * math.pi * frequency * current_time.to_sec()) for i in range(6)]
        point.positions = joint_positions
        point.time_from_start = rospy.Duration(1.0)

        joint_traj_msg.points.append(point)

        pub.publish(joint_traj_msg)
        rate.sleep()

if __name__ == '__main__':

        amplitudes = rospy.get_param('~amplitudes', [1.5, 1.5, 1.5, 1.5, 1.5, 0.1])
        frequency = rospy.get_param('~frequency', 1.0)
        try:
            publish_sine_wave_positions(amplitudes, frequency)
        except rospy.ROSInterruptException:
            pass


