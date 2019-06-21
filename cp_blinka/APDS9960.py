#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for adafruit-circuitpython-apds9960.

    based on
    https://learn.adafruit.com/adafruit-apds9960-breakout/circuitpython

"""

import time

import board
import busio

import adafruit_apds9960.apds9960

print("apds9960 i2c tests")

print("setup i2c")
i2c = busio.I2C(board.SCL, board.SDA)

print("setup APDS9960")
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

print("read proximity")
sensor.enable_proximity = True
for index in range(12):
    print(sensor.proximity())
    time.sleep(0.25)

print("read color")
sensor.enable_color = True
r, g, b, c = sensor.color_data
print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

print("waiting for gesture...")
gesture_name = {
    0: "No",
    1: "Up",
    2: "Down",
    3: "Left",
    4: "Right",
}
sensor.enable_gesture = True

for index in range(4):
    gesture = sensor.gesture()
    while gesture == 0:
        gesture = sensor.gesture()
    print('Saw gesture: {}: {}'.format(gesture, gesture_name[gesture]))
    print("waiting for gesture...")
