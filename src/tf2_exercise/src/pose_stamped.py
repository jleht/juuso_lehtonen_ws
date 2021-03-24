#! /usr/bin/python3

import rospy
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import math
import turtlesim.msg
import tf_conversions
import subprocess



def callback(data):
    msg = geometry_msgs.msg.PoseStamped()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = "world"
    msg.pose.position.x = data.x
    msg.pose.position.y = data.y
    quaternion = tf_conversions.transformations.quaternion_from_euler(0,0, data.theta)
    msg.pose.orientation.w = quaternion[0]
    msg.pose.orientation.x = quaternion[1]
    msg.pose.orientation.y = quaternion[2]
    msg.pose.orientation.z = quaternion[3]
    turtle_vel.publish(msg)


if __name__ == '__main__':
    rospy.init_node('pose_stamped')

    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)

    turtle_name = rospy.get_param('turtle', 'turtle2')
    turtle_vel = rospy.Publisher('%s/pose_stamped' % turtle_name, geometry_msgs.msg.PoseStamped, queue_size=1)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            trans = tf_buffer.lookup_transform('turtle2', 'turtle1', rospy.Time())
            trans2 = tf_buffer.lookup_transform('turtle3', 'turtle1', rospy.Time())

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        rospy.Subscriber('turtle2/pose',turtlesim.msg.Pose,callback)
        if trans.transform.translation.x > -0.2 and trans.transform.translation.x < 0.2\
            and trans.transform.translation.y > -0.2 and trans.transform.translation.x < 0.2:
            print("Warning! Turtle2 is close to turtle1")
        if trans2.transform.translation.x > -0.2 and trans2.transform.translation.x < 0.2\
            and trans2.transform.translation.y > -0.2 and trans2.transform.translation.x < 0.2:
            print("Warning! Turtle3 is close to turtle1, stopping turtle1")
            subprocess.call(["rosnode", "kill", "/randomwalk"]) #There is probably a better way to do this by killing the node with some rospy method?

        rate.sleep()
