#!/usr/bin/env python
from my_robot.srv import Oint_ControlRequest, Oint_Control

import rospy
from math import pi,sin,cos
rospy.init_node('elipse')
move = rospy.ServiceProxy('/oint_control_srv',Oint_Control)
period = 8.0
pub = rospy.Publisher('square_pub',Oint_ControlRequest,queue_size=10)
rate_t = 20
rate = rospy.Rate(rate_t)
msg = Oint_ControlRequest()

msg.time = 5
a = 0.4
b = 0.2
msg.pos[0] = sin(2*pi*((rospy.Time.now().to_sec()+5.)%period)/period)*a
msg.pos[1] = cos(2*pi*((rospy.Time.now().to_sec()+5.)%period)/period)*b
msg.pos[2] = 0.3
msg.rpy = [0,0,0]
msg.mode = 1
move(msg)
msg.time = 1./rate_t
while not rospy.is_shutdown():
    th = 2*pi*(rospy.Time.now().to_sec()%period)/period
    msg.pos[0] = sin(th)*a
    msg.pos[1] = cos(th)*b
    msg.pos[2] = 0.3
    move(msg)
    rate.sleep()


