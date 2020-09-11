#!/usr/bin/env python

from miflora_server.srv import *
from miflora_msgs.msg import * 
import rospkg
import rospy
import sys
import subprocess
import json 

sensor_pub = rospy.Publisher('/miflora', miflora, queue_size=10)
sensor_msg = miflora()

def callback_msg(msg):
  ''' Read sensor and return measurements '''

  # Run sensor driver.  Requires python >=3.6
  # HACK: Done this way to remove conflicts with ROS python version.
  path = rospkg.RosPack().get_path('miflora_server')
  miflora_out = subprocess.check_output(["python3.7", path+"/src/miflora_driver.py", msg.MAC])
    
  try:
    miflora_data = json.loads(miflora_out.replace("'", '"'))
    response = read_mifloraResponse()
    response.sensor.header.stamp = rospy.Time.now()
    response.sensor.header.frame_id = msg.FrameID
    response.sensor.moisture = miflora_data['soil-moisture']
    response.sensor.battery = miflora_data['battery']
    response.sensor.illuminance = miflora_data['light']
    response.sensor.temperature = miflora_data['soil-temperature']
    response.sensor.conductivity = miflora_data['soil-ec']

    # Publish reading to topic
    sensor_msg = response.sensor
    sensor_pub.publish(sensor_msg)

    # Return reading to service client
    return response

  except:
    # Return blank measurements on error.
    rospy.logerr(miflora_out)
    rospy.logwarn("Try resetting BL: $ sudo hciconfig hci0 down && sudo hciconfig hci0 up")
    return read_mifloraResponse()


def service_server():
  rospy.init_node("sensor_server")
  s = rospy.Service("sensor_read", read_miflora, callback_msg)
  rospy.spin()


if __name__ == "__main__":
  service_server()