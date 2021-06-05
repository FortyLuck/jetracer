#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Joy
from jetracer.nvidia_racecar import NvidiaRacecar

CAR = NvidiaRacecar()


def callback(data):
    CAR.steering = float(data.axes[0])
    CAR.throttle = float(data.axes[1])


if __name__ == '__main__':
    rospy.init_node('jetracer_joy_teleop')
    rospy.Subscriber('joy', Joy, callback)
    rospy.spin()
