MiFlora
====================

ROS package for reading the MiFlora plant sensor.
![Foto MiFlora](http:// )
Bluetooth monitor for light, moisture, electric conductivity, and temperature.

Install instructions

Requires python > 3.6
<pre>
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt-get install python3.7
</pre>
<pre>
sudo apt-get install python-pip libglib2.0-dev
sudo python3.7 -m pip install miflora
sudo python3.7 -m pip install bluepy
</pre>

Set permission so the app can use Bluetooth
<pre>
$ find /usr/local/lib -name bluepy-helper
or
$ find /home -name bluepy-helper

$ sudo setcap cap_net_raw+e  <PATH>/bluepy-helper
$ sudo setcap cap_net_admin+eip  <PATH>/bluepy-helper

Where <PATH> is the place where bluepy-helper is installed.

</pre>

Install the ROS package
<pre>
catkin_ws/src$ git clone 
catkin_ws/src$ cd ..
catkin_ws$ catkin build
catkin_ws$ source devel/setup.bash
</pre>

Discover the MAC address of your sensor.
<pre>
catkin_ws$ rosrun miflora_service discover_devices.py

This will print out the MAC address if found.
00:00:00:00:00:00
</pre>

Edit the launch file and update with MAC address and name.
<pre>
catkin_ws$ rosedit miflora_service service.launch
</pre>

```
    <arg name="Frame_ID" default="MEASUREMENT_FRAME"/>
    <arg name="MAC_addr" default="00:00:00:00:00:00"/>
    <!-- Sample Rate miniumum is twice per minute 2 hz -->
    <arg name="sample_rate" default="2"/>
```






