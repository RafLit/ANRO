#!/usr/bin/env python
from my_robot.srv import Oint_ControlRequest, Oint_Control

import rospy

rospy.init_node('square')
rospy.wait_for_service('/oint_control_srv')
move = rospy.ServiceProxy('/oint_control_srv',Oint_Control)
rate_t = 0.5
rate = rospy.Rate(rate_t)
c1 = Oint_ControlRequest()
c2 = Oint_ControlRequest()
c3 = Oint_ControlRequest()
c4 = Oint_ControlRequest()
c1.time = c2.time = c3.time = c4.time = 1./rate_t
c1.pos = [0.3, 0.3, 0.4]
c2.pos = [0.3, -0.3, 0.4]
c3.pos = [-0.3, -0.3, 0.4]
c4.pos = [-0.3, 0.3, 0.4]
start = Oint_ControlRequest()
start.pos = c4.pos
start.time = 5
c1.rpy = c2.rpy = c3.rpy = c4.rpy = [0,0,0]
c1.mode = c2.mode = c3.mode = c4.mode = 0
move(start)
while not rospy.is_shutdown():
    for posi in [c1,c2,c3,c4]:
        move(posi)
        rate.sleep()
