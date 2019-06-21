#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for adafruit-circuitpython-apds9960.

    based on
    https://learn.adafruit.com/adafruit-apds9960-breakout/circuitpython

"""

import board
import busio

print("basic i2c tests")
with busio.I2C(SCL, SDA) as i2c:
    print(i2c.scann())
