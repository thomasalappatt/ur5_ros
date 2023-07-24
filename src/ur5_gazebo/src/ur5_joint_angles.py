#!/usr/bin/python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def publish_positions(joint_positions):
    # Rest of the code remains the same as in your original script
    rospy.init_node('position_publisher_node', anonymous=True)
    pub = rospy.Publisher('/eff_joint_traj_controller/command', JointTrajectory, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        joint_traj_msg = JointTrajectory()
        joint_traj_msg.joint_names = ["elbow_joint", "shoulder_lift_joint", "shoulder_pan_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]

        point = JointTrajectoryPoint()
        point.positions = joint_positions
        point.time_from_start = rospy.Duration(1.0)

        joint_traj_msg.points.append(point)

        pub.publish(joint_traj_msg)
        rate.sleep()

if __name__ == '__main__':
    if len(sys.argv) != 7:  # Note that there should be 7 arguments (including the script name itself)
        print("Usage: python ur5_joint_angles.py <elbow_joint> <shoulder_lift_joint> <shoulder_pan_joint> <wrist_1_joint> <wrist_2_joint> <wrist_3_joint>")
    else:
        joint_positions = [float(arg) for arg in sys.argv[1:]]
        try:
            publish_positions(joint_positions)
        except rospy.ROSInterruptException:
            pass
