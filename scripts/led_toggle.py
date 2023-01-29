#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import Jetson.GPIO as GPIO

output_pin = 12 #pin 12
if __name__ == '__main__':
    rospy.init_node('led_toggle', anonymous=True)
    mode = 0

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(output_pin,GPIO.OUT,initial=GPIO.LOW)

    while not rospy.is_shutdown():
        msg = rospy.wait_for_message("/Signal", Int32, timeout=None)
        mode = msg.data
        if mode == 1:
            curr_value = GPIO.HIGH
        elif mode == 0:
            curr_value = GPIO.LOW
        print(curr_value)
        GPIO.output(output_pin,curr_value)

    GPIO.cleanup()