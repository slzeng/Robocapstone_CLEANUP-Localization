



#include <tf/transform_listener.h>
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>


// void dynamics_sim(){

// }

int main(int argc, char** argv){
  ros::init(argc, argv, "fake_pose");
  
  ros::NodeHandle node;
  ros::Rate loop_rate(20);

  static tf::TransformBroadcaster br;
  tf::TransformListener listener;  
  tf::Transform transform;
  tf::Quaternion q;
  
  // ros::Subscriber sub = n.subscribe("chatter", 1000, );

  while(ros::ok())
  {
    // tf::StampedTransform transform;
    // try{
    //   listener.lookupTransform("/world", "/target",  
    //                            ros::Time(0), transform);
    // }
    // catch (tf::TransformException ex){
    //   ROS_ERROR("%s",ex.what());
    //   ros::Duration(1.0).sleep();
    // }



    transform.setOrigin( tf::Vector3(0, 0, 0));
    q.setRPY(0, 0, 0);
    transform.setRotation(q);
    br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "/world", "/robot"));

    ros::spinOnce();

    loop_rate.sleep();
  }
  return 0;
};