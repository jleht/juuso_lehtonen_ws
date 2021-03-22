#! /usr/bin/python3

import rospy
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import math
import turtlesim.msg
import tf_conversions

def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = turtlename
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)


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

    print(data.theta)

if __name__ == '__main__':
    rospy.init_node('pose_stamped')

    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)

    turtle_name = rospy.get_param('turtle', 'turtle2')
    turtle_vel = rospy.Publisher('%s/pose_stamped' % turtle_name, geometry_msgs.msg.PoseStamped, queue_size=1)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            trans = tf_buffer.lookup_transform(turtle_name, 'turtle1', rospy.Time())
            print("test1")
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            print("test2")
            continue
        rospy.Subscriber('turtle2/pose',turtlesim.msg.Pose,callback)
        
        rate.sleep()
