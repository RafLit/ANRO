#!/usr/bin/env python
import rospy
import copy
from sympy import *
from tf.transformations import *
from math import atan2,atan,acos,asin,sin,cos,sqrt,pi
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped

a = 0.5
b = 0.5
rospy.init_node('IKIN')
pub = rospy.Publisher('/joint_states',JointState,queue_size = 10)
def callback(msg):
    global pub
    global a,b
    x0 = msg.pose.position.x
    y0 = msg.pose.position.y
    z0 = msg.pose.position.z
    pub_msg = JointState()
    try:
        th0 = atan2(y0,x0)
    except:
        rospy.logerr("wrong position")
        return
    try:
        th2 = acos(-(x0**2 + y0**2 +z0**2-a**2 -b**2)/(2*a*b)*0.999999999999999)

    except:
        rospy.logerr("wrong position")
        return
    th2x = pi - th2
    sthx = sin(th2x)
    cthx = cos(th2x)
    cth0 = cos(th0)
    sth1 = (b*cth0*z0 + a*sthx*x0 + a*cth0*cthx*z0)/(cth0*(a**2*cthx**2 + a**2*sthx**2 + 2*a*b*cthx + b**2))
    cth1 = (b*x0 + a*cthx*x0 - a*cth0*sthx*z0)/(cth0*(a**2*cthx**2 + a**2*sthx**2 + 2*a*b*cthx + b**2))
    try:
        th1 = atan2(sth1,cth1)
    except:
        rospy.logerr("wrong position")
        return
        
    pub_msg.name = ['joint1','joint2','joint3']
    pub_msg.position = [th0, -th1, th2x]
    pub_msg.header.stamp = rospy.Time.now()
    pub_msg.header.frame_id = 'manipulator'
    pub.publish(pub_msg)


sub = rospy.Subscriber('/oint_pos',PoseStamped,callback)
rospy.spin()
