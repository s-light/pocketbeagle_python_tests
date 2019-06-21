#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""simple test for Adafruit_BBIO GPIO."""

import sys
import time

import Adafruit_BBIO.GPIO as GPIO

# print python version - just so we know what we are using ;-)
print(sys.version)

mypin = "USR3"
GPIO.setup(mypin, GPIO.OUT)

print(mypin, "blink...")

try:
    while True:
        GPIO.output(mypin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(mypin, GPIO.LOW)
        time.sleep(0.5)
except Exception as e:
    raise e
finally:
    print("cleanup")
    GPIO.output(mypin, GPIO.LOW)
    GPIO.cleanup()
