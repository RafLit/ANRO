#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped, Quaternion, Point
import sys
import PyKDL

rospy.init_node( 'KDL_DKIN')
baseFrame = PyKDL.Frame(PyKDL.Vector(0,0,0.3))
params = rospy.get_param('/arm')
s1, s2, s3 = (params["s1"], params["s2"], params["s3"])
frame1 = PyKDL.Frame().DH(s2['a'],s2['al'],s1['d'],s1['th'])
frame2 = PyKDL.Frame().DH(s3['a'],s3['al'],s2['d'],s2['th'])
frame3 = PyKDL.Frame().DH(0,0,s3['d'],s3['th'])
chain = PyKDL.Chain()
segment0 = PyKDL.Segment(PyKDL.Joint(),baseFrame)
segment1 = PyKDL.Segment(PyKDL.Joint(PyKDL.Joint.RotZ),frame1)
segment2 = PyKDL.Segment(PyKDL.Joint(PyKDL.Joint.RotZ),frame2)
segment3 = PyKDL.Segment(PyKDL.Joint(PyKDL.Joint.RotZ),frame3)
chain.addSegment(segment0)
chain.addSegment(segment1)
chain.addSegment(segment2)
chain.addSegment(segment3)
solver = PyKDL.ChainFkSolverPos_recursive(chain)
jointArray = PyKDL.JntArray(chain.getNrOfJoints())
pub = rospy.Publisher('kdl_dkin_pose',PoseStamped, queue_size=10)

def jointStateCallback(msg):
    if msg.position[1] > 0.5:
        rospy.logerr("joint 2 has reached its limit!")
        return
    if not -1.57 < msg.position[2] < 1.57:
        rospy.logerr("joint 3 has reached its limit!")
        return
    jointArray[0] = msg.position[0]
    jointArray[1] = msg.position[1]
    jointArray[2] = msg.position[2]
    finFrame = PyKDL.Frame()
    solver.JntToCart(jointArray,finFrame)
    mani_frame = finFrame
    pos_kdl = mani_frame.p
    pos_msg = Point(*pos_kdl)
    rot_kdl = mani_frame.M
    rot_msg = Quaternion(*rot_kdl.GetQuaternion())
    pub_msg = PoseStamped()
    pub_msg.header.stamp = rospy.Time.now()
    pub_msg.header.frame_id = 'base_link'
    pub_msg.pose.position = pos_msg
    pub_msg.pose.orientation = rot_msg
    pub.publish(pub_msg)

sub = rospy.Subscriber('/joint_states',JointState, jointStateCallback)
rospy.spin()
