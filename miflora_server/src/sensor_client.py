#!/usr/bin/env python

import rospy
from miflora_server.srv import *


def publish_sensor():
  # Load parameters set in launch file
  frame_id = rospy.get_param('~Frame_ID', "greenhouse") 
  mac_addr = rospy.get_param('~MAC_addr', "00:00:00:00:00:00")
  sample_rate = rospy.get_param('~sample_rate', "0.01667")

  # Setup call to ROS Service
  rospy.wait_for_service("sensor_read")
  service_client = rospy.ServiceProxy("sensor_read", read_miflora)
  service_client_object = read_mifloraRequest()
  service_client_object.FrameID = frame_id
  service_client_object.MAC = mac_addr

  rate = rospy.Rate(sample_rate)

  while not rospy.is_shutdown():
    # Call service and get response 
    result = service_client(service_client_object)
    rospy.loginfo(result)
    rate.sleep()

  rospy.spin()       


if __name__ == '__main__':
  rospy.init_node('miflora_service_client')

  try:
      publish_sensor()
  except rospy.ROSInterruptException:
      pass