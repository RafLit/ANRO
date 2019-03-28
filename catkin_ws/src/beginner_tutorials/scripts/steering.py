#!/usr/bin/env python
import click
import rospy
from geometry_msgs.msg import Twist 
rospy.init_node('steering')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
front = rospy.get_param("/front")
back = rospy.get_param("/back")
left = rospy.get_param("/left")
right = rospy.get_param("/right")
print right
while not rospy.is_shutdown():

    msg = Twist()
    key = click.getchar()
    if key == front:
        msg.linear.x = 1
    elif key == right:
        msg.angular.z = -1
    elif key == back:
        msg.linear.x = -1
    elif key == left:
        msg.angular.z = 1
    pub.publish(msg)
