cmake_minimum_required(VERSION 2.8.3)
project(my_robot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation
  sensor_msgs
  geometry_msgs
  std_msgs
  tf
  visualization_msgs
)
find_package(orocos_kdl REQUIRED)

 add_service_files(
   FILES
   Jint_Control.srv
   Oint_Control.srv
 )

 generate_messages(
   DEPENDENCIES
   sensor_msgs   std_msgs   geometry_msgs
 )
catkin_package(
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
