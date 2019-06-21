#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""simple test for Adafruit_BBIO PWM."""

import sys
import time

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

print(sys.version)

my_led = "USR3"
GPIO.setup(my_led, GPIO.OUT)

my_pwm = "P1_36"
PWM.start(my_pwm, 50, 1000)

print(my_pwm, "PWM running.....")


##########################################

try:
    while True:
        GPIO.output(my_led, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(my_led, GPIO.LOW)
        time.sleep(0.5)
        print("\nenter new frequency in MHz: ")
        new_value = input()
        new_freq_Hz = 1000
        try:
            new_freq_Hz = int(float(new_value) * 1000 * 1000)
        except ValueError as e:
            print("Exception: ", e)
        print(
            "calculated frequency: \n"
            "{:}MHz (= {:}Hz)"
            "".format(
                new_freq_Hz / (1000*1000),
                new_freq_Hz
            )
        )
        PWM.set_frequency(my_pwm, new_freq_Hz)
        PWM.set_duty_cycle(my_pwm, 50)
except KeyboardInterrupt:
    print("exit")
finally:
    print("cleanup")

    GPIO.output(my_led, GPIO.LOW)
    GPIO.cleanup()

    PWM.stop(my_pwm)
    PWM.cleanup()
