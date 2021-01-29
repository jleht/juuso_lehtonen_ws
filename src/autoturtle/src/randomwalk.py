#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

def callback(data):
    vel_msg = Twist()
    pose = data
    turn_list = [-45,45]
    print(pose.theta)
    if pose.theta > 0.785 and pose.theta < 2.355 and (pose.y > 10 or pose.x > 10):
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1
        print("a")
    elif (pose.theta > 2.355 or pose.theta < -2.355) and (pose.x < 1 or pose.y > 10):
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1

        print("b")

    elif pose.theta > -2.355 and pose.theta < -0.785 and (pose.y < 1 or pose.x < 1):
        vel_msg.angular.z = random.choice(turn_list)
        print("c")
        vel_msg.linear.x = 1

    elif pose.theta > -0.785 and pose.theta < 0.785 and (pose.x > 10 or pose.y < 1):
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1

        print("d")
    elif (pose.theta < -2.355 or pose.theta > 2.355) and pose.y < 1:
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1
        print("e")
    elif pose.theta < 2.355 and pose.theta > 0.785 and pose.x < 1:
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1
        print("f")
    elif pose.theta < 0.785 and pose.theta > -0.785 and pose.y > 10:
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1
        print("g")
    elif pose.theta < -0.785 and pose.theta > -2.355 and pose.x > 10:
        vel_msg.angular.z = random.choice(turn_list)
        vel_msg.linear.x = 1
        print("h")
    else:
        vel_msg.linear.x = 6
        vel_msg.angular.z = random.uniform(-4,4)
        print("else")





    velocity_publisher.publish(vel_msg)


rospy.init_node('turtlebot_auto', anonymous=True)
velocity_publisher = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)
pose_subscriber = rospy.Subscriber('turtle1/pose',Pose,callback)

while not rospy.is_shutdown():
    rospy.spin()
