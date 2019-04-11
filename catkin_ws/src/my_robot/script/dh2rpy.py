import json
from tf.transformations import *
import rospy
import sys
x_ax = (1,0,0)
y_ax = (0,1,0)
z_ax = (0,0,1)

def convert(filename):
    params = {}
    with open(filename, 'r') as file:
        params=json.loads(file.read())

    with open('../dhparams.yaml', 'w') as file:
        for key in params.keys():
            a, d, al, th = params[key]
            a, d, al, th = map(float, (a, d, al, th))

            trans_z = translation_matrix((0,0,d))
            rot_z = rotation_matrix(th, z_ax)
            trans_x = translation_matrix((a,0,0))
            rot_x = rotation_matrix(al, x_ax)

            mat = concatenate_matrices(trans_z, rot_z, trans_x, rot_x)

            (roll, pitch, yaw) = euler_from_matrix(mat)
            (x,y,z) = translation_from_matrix(mat)

            file.write(key + ":\n")
            file.write("    joint_xyz: {} {} {}\n".format(x,y,z))
            file.write("    joint_rpy: {} {} {}\n".format(roll, pitch, yaw))
            file.write("    link_xyz: {} 0 0\n".format(x/2))
            file.write("    link_rpy: 0 0 0\n")
            file.write("    link_l: {}\n".format(a))



if __name__ == '__main__':
    convert("../dhpars.json")


