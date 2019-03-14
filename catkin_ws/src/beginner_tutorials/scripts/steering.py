#!/usr/bin/env python
import click
import rospy
from geometry_msgs.msg import Twist 
rospy.init_node('steering')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():

    msg = Twist()
    key = click.getchar()
    if key == 'w':
        msg.linear.x = 1
    elif key == 'a':
        msg.angular.z = 1
    elif key == 's':
        msg.linear.x = -1
    elif key == 'd':
        msg.angular.z = -1
    pub.publish(msg)
