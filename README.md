MiFlora
====================

ROS package for reading the MiFlora plant sensor. <br />


ROS package freezes bluetooth adapter and stops working frequently. <br />
Any ideas?  Please open pull request or open issue. <br />


![Foto MiFlora](https://github.com/ros-agriculture/miflora_ros/blob/master/miflora.png?raw=true ) <br />
Bluetooth monitor for light, moisture, electric conductivity, and temperature.

### Install instructions

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

### Set permission so the app can use Bluetooth
<pre>
$ find /usr/local/lib -name bluepy-helper
or
$ find /home -name bluepy-helper

$ sudo setcap cap_net_raw+e  **PATH**/bluepy-helper
$ sudo setcap cap_net_admin+eip  **PATH**/bluepy-helper

Where **PATH** is the place where bluepy-helper is installed.

</pre>

### Install the ROS package
<pre>
catkin_ws/src$ sudo apt-get install python-catkin-tools
catkin_ws/src$ git clone https://github.com/ros-agriculture/miflora_ros.git
catkin_ws/src$ cd ..
catkin_ws/src$ rosdep install --from-paths src --ignore-src --rosdistro ${ROS_DISTRO}
catkin_ws$ catkin build
catkin_ws$ source devel/setup.bash
</pre>

### Discover the MAC address of your sensor.
<pre>
catkin_ws$ rosrun miflora_server discover_devices.py

This will print out the MAC address if found.
00:00:00:00:00:00
</pre>

### Edit the launch file and update with MAC address and name.
<pre>
catkin_ws$ rosedit miflora_server client.launch
</pre>

```
    <arg name="Frame_ID" default="MEASUREMENT_FRAME"/>
    <arg name="MAC_addr" default="00:00:00:00:00:00"/>
    <!-- Sample Rate minimum is once per minute 0.01667 hz -->
    <arg name="sample_rate" default="0.01667"/>
```

### Running the Node

Start ROS Service
<pre>
catkin_ws$ roslaunch miflora_server service.launch
</pre>

Start the ROS Service Client to request readings
<pre>
catkin_ws$ roslaunch miflora_server client.launch
</pre>

Start both the service and client
<pre>
catkin_ws$ roslaunch miflora_server read_sensor.launch
</pre>


### Troubleshooting:
![Foto MiFlora Error](https://github.com/ros-agriculture/miflora_ros/blob/master/error.png?raw=true)

If your raspberry pi stops being able to connect to the sensor run:
<pre>
$ sudo hciconfig hci0 down && sudo hciconfig hci0 up
</pre>

The BLE device freezes a lot on a raspberrypi 3.
Adding this crontab job will reset your BLE at a regular interval.
<pre>
$ sudo crontab -e

This will open a edit window.  Then add this at the bottom:

5 * * * * hciconfig hci0 reset

</pre>







