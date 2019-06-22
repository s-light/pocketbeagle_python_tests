#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for adafruit-circuitpython-apds9960.

    based on
    https://circuitpython.readthedocs.io/projects/cap1188/en/latest/examples.html

"""

import time

import board
import busio

from adafruit_cap1188.i2c import CAP1188_I2C

print("CAP1188 i2c tests")

print("setup i2c")
i2c = busio.I2C(board.SCL, board.SDA)

print("setup CAP1188")
cap = CAP1188_I2C(i2c)

while True:
    for i in range(1, 9):
        if cap[i].value:
            print("Pin {} touched! ({})".format(i, cap[i].raw_value))
