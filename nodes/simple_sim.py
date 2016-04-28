#!/usr/bin/env python
import roslib;
roslib.load_manifest('localization')
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Point
import tf
from tf import TransformerROS
import math
from visualization_msgs.msg import Marker

class Sim(object):
    """docstring for Sim"""
    def __init__(self):
        rospy.init_node('simple_sim', anonymous=True)
        rospy.Subscriber("/cmd", Pose2D, self.sim_callback)
        self.cam_point_pub = rospy.Publisher('/cam_points', Marker, queue_size=10)
        
        
        self.x = 7;
        self.y = 7;
        self.z = 0;
        self.theta = 0;
        self.t_init = rospy.Time.now().to_sec();
        self.t_prev = rospy.Time.now().to_sec();
        self.t = rospy.Time.now().to_sec();
        
        self.camera_height = .4;
        
        self.br = tf.TransformBroadcaster()

        self.camera_fov_x = .15;
        self.camera_fov_y = .31;

        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            self.br.sendTransform((self.x, self.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, self.theta),
                     rospy.Time.now(),
                     "/robot",
                     "/world")                       
            
            self.br.sendTransform((0, 0, self.camera_height),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     "/camera",
                     "/robot")

            self.br.sendTransform((-.1, 0, 0),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     "/eliminator",
                     "/robot")    
            rate.sleep()    
            




    def sim_callback(self, data):
        self.t_prev = self.t;
        self.t = rospy.Time.now().to_sec();
        dt = self.t-self.t_prev;

        if(data.x > .5):
            print("PAST MAX VEL: %f",data.x)
            data.x = .5;
        if(data.theta > 1):
            print("PAST MAX OMEGA: %f", data.theta)
            data.theta = 1;
        self.x += data.x*dt*math.cos(self.theta);
        self.y += data.x*dt*math.sin(self.theta);
        self.theta += data.theta*dt;
        # print(self.x,self.y,self.theta)
        
        


if __name__ == '__main__':
    s = Sim();