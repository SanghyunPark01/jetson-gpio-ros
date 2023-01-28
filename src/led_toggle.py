#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO

def callback(data):
    mode = data.data

output_pin = 18 #pin 12
if __name__ == '__main__':
    rospy.init_node('led_toggle', anonymous=True)
    mode = 0
    rospy.Subscriber("/Signal", Int32, callback)
    rate = rospy.Rate(1000)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(output_pin,GPIO.OUT,initial=GPIO.LOW)

    while not rospy.is_shutdown():
        if mode == 1:
            curr_value = GPIO.HIGH
        elif mode == 0:
            curr_value = GPIO.LOW

        GPIO.output(output_pin,curr_value)

        rate.sleep()
        rospy.spinOnce()

    GPIO.cleanup()