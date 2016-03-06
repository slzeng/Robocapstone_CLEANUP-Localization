cmake_minimum_required(VERSION 2.8.3)
project(localization)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg tf)

## Declare ROS messages and services
# add_message_files(DIRECTORY msg FILES Num.msg)
# add_service_files(DIRECTORY srv FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(fake_pose_node src/fake_pose.cpp)
target_link_libraries(fake_pose_node ${catkin_LIBRARIES})
