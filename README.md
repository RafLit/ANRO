# ANRO

the main package is my_robot<br/>
the robot is generated from dh parameters, stored in param directory

### launching:
* Simple, movable model, forward kinematics:
```
roslaunch my_robot movable.launch
```
* Robot movement interpolation:
```
roslaunch my_robot jint.launch
```
and then:
```
rosservice call /jint_control_srv "mode: 0
time: 10.0
pos:
- 5.0
- -0.5
- 0.3"
```
for third-degree function interpolation change the mode to 1

* Movement interpolation:
```
roslaunch my_robot oint.launch
```
and then:
```
rosservice call /oint_control_srv "mode: 0
time: 10.0
pos:
- 5.0
- 2.0
- 1.0"
```
for third-degree function interpolation change the mode to 1

for demonstration run:
```
roslaunch my_robot ointSquare.launch
```
or:
```
roslaunch my_robot ointEllipse.launch
```

* Inverse kinematics:
```
roslaunch my_robot ikinEllipse.launch
```
or:
```
roslaunch my_robot ikinSquare.launch
```


