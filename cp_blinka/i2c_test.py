#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for adafruit-circuitpython-apds9960.

    based on
    https://circuitpython.readthedocs.io/en/latest/shared-bindings/busio/I2C.html#busio.I2C
    https://circuitpython.readthedocs.io/projects/busdevice/en/latest/api.html#adafruit-bus-device-i2c-device-i2c-bus-device

"""

import board
import busio

print("basic i2c tests")
with busio.I2C(board.SCL, board.SDA) as i2c:
    print(i2c.scan())
