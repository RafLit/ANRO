#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped, Quaternion, Point
import sys
from tf.transformations import *

xax = (1,0,0)
yax = (0,1,0)
zax = (0,0,1)
rospy.init_node( 'NONKDL_DKIN')
pub = rospy.Publisher('nonkdl_dkin_pose',PoseStamped, queue_size=10)
params = rospy.get_param('/arm')
s1, s2, s3 = (params['s1'],params['s2'],params['s3'])

def jointStateCallback(msg):
    if msg.position[1] > 0.5:
        rospy.logerr("joint 2 has reached its limit!")
        return
    if not -1.57 < msg.position[2] < 1.57:
        rospy.logerr("joint 3 has reached its limit!")
        return
    s1['th'] = msg.position[0]
    s2['th'] = msg.position[1]
    s3['th'] = msg.position[2]
    mats = []
    mats.append(translation_matrix((0,0,0.3)))
    for s in [s1,s2,s3]:
        rotAl = rotation_matrix(s['al'],xax)
        transA = translation_matrix((s['a'],0,0))
        rotTh = rotation_matrix(s['th'],zax)
        transd = translation_matrix((0,0,s['d']))
        mats.append(concatenate_matrices(rotAl,transA,rotTh,transd))
    mat = concatenate_matrices(*mats)
    quat = Quaternion(*quaternion_from_matrix(mat))
    trans = Point(*translation_from_matrix(mat))
    pub_msg = PoseStamped()
    pub_msg.header.stamp = rospy.Time.now()
    pub_msg.header.frame_id = 'base_link'
    pub_msg.pose.position = trans
    pub_msg.pose.orientation = quat
    pub.publish(pub_msg)
sub = rospy.Subscriber('/joint_states',JointState,jointStateCallback)
rospy.spin()












