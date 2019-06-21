#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for adafruit-blinka.

    https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
"""

import board
import digitalio
import busio

print("Hello blinka!")

# Try to great a Digital input
# pin = digitalio.DigitalInOut(board.LED_USR3)
pin = digitalio.DigitalInOut(board.P1_2)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")
i2c = busio.I2C(board.SCL_2, board.SDA_2)
print("I2C_2 ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")
spi = busio.SPI(board.SCLK_1, board.MOSI_1, board.MISO_1)
print("SPI_1 ok!")

print("done!")
