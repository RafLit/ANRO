#!/usr/bin/env python
import rospy
import copy
from sympy import *
from tf.transformations import *

def prmat(mat):
    a = mat.tolist()
    for i in a:
        print i
        pass
    o = []
    for i in range(3):
        o.append(a[i][3])
    return o

s1 = Symbol('s1')
c1 = Symbol('c1')
s2 = Symbol('s2')
c2 = Symbol('c2')
s3 = Symbol('s3')
c3 = Symbol('c3')
px = Symbol('px')
py = Symbol('py')
pz = Symbol('pz')

T01 = Matrix([[s1,c1,0,0],[c1,-s1,0,0],[0,0,1,0],[0,0,0,1]])
T12 =  rotation_matrix(-pi/.4,(1,0,0))*Matrix([[s2,c2,0,0],[c2,-s2,0,0],[0,0,1,0],[0,0,0,1]])
T23 = translation_matrix((0.4,0,0))*Matrix([[s3,c3,0,0],[c3,-s3,0,0],[0,0,1,0],[0,0,0,1]])
T34 = translation_matrix((0.1,0,0))
o = prmat(T12*T23*T34)
T0n = Matrix([[1,0,0,px],[0,1,0,py],[0,0,1,pz],[0,0,0,1]])
print prmat(T01**-1*T0n)
y = prmat(T12*T23*T34)
print y
prmat(T34)

al = 0.4/y[1].evalf(subs={c2:1})
e = 1./y[2].evalf(subs={c2:1})
#with open('../param/invparams.yaml','w') as file:
 #   file.write("alpha: {:.20f}\n".format(al))
  #  file.write("beta: {:.20f}".format(e))








