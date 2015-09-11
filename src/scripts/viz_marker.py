import roslib
from visualization_msgs.msg import Marker
import rospy
import math

topic = "/viz_marker"
publisher = rospy.Publisher(topic, Marker, queue_size=10)
rospy.init_node('register')

marker = Marker()
marker.type = marker.SPHERE
marker.action = marker.ADD
marker.scale.x = 0.2
marker.scale.y = 0.2
marker.scale.z = 0.2
marker.color.a = 1.0
marker.color.r = 1.0
marker.color.g = 1.0
marker.color.b = 0.0
marker.pose.orientation.w = 1.0
marker.pose.position.x = math.cos(count / 50.0)
marker.pose.position.y = math.cos(count / 40.0) 
marker.pose.position.z = math.cos(count / 30.0) 

r = rospy.Rate(10)
while not rospy.is_shutdown():
  publisher.publish(marker)
  r.sleep()