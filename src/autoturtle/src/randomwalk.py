#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

def callback(data):
    vel_msg = Twist()
    pose = data
    print(pose.theta)
    if pose.x > 10:
        vel_msg.angular.z = random.randint(-5,0)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 5


    elif pose.x < 1:
        vel_msg.angular.z = random.randint(-5,0)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 5

    elif pose.y > 10:
        vel_msg.angular.z = random.randint(-5,0)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 5

    elif pose.y < 1:
        vel_msg.angular.z = random.randint(-5,0)
        vel_msg.linear.x = 0
        vel_msg.linear.y = 5
    
    else:
        vel_msg.angular.z = 0
        vel_msg.linear.x = 0
        vel_msg.linear.y = 5

    velocity_publisher.publish(vel_msg)


rospy.init_node('turtlebot_auto', anonymous=True)
velocity_publisher = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)
pose_subscriber = rospy.Subscriber('turtle1/pose',Pose,callback)

while not rospy.is_shutdown():
    rospy.spin()
