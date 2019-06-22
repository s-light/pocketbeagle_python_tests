#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for adafruit-circuitpython-ssd1306.

    based on
    https://learn.adafruit.com/adafruit-oled-featherwing/circuitpython-and-python-usage#full-example-code-8-40
    https://learn.adafruit.com/circuitpython-oled-knob-sketcher/drawing-pixels#its-full-of-stars-3-18

    check pin settings
    https://github.com/adafruit/adafruit-beaglebone-io-python#spi

    SPI0
    ```bash
    # SPI0_CS0:
    $ config-pin P1_6 spi_cs
    # SPI0_SCLK:
    $ config-pin P1_8 spi_sclk
    # SPI0_D0:
    $ config-pin P1_10 spi
    # SPI0_D1:
    $ config-pin P1_12 spi
    ```
"""

import time
import random

import board
import digitalio
import busio

import adafruit_ssd1306

print("oled display tests")

print("setup spi")
spi = busio.SPI(board.SCLK, board.MOSI)
print("setup digitalio")
pin_cs = digitalio.DigitalInOut(board.P2_6)
pin_rst = digitalio.DigitalInOut(board.P1_2)
pin_dc = digitalio.DigitalInOut(board.P1_4)

print("init SSD1306_SPI")
width = 128
height = 64
# width, height, spi, dc, reset, cs
display = adafruit_ssd1306.SSD1306_SPI(
    width, height, spi, pin_dc, pin_rst, pin_cs)

print("clear display")
display.fill(0)
display.show()

print("fill display")
display.fill(1)
display.show()
time.sleep(2)
display.fill(0)

print("draw some test pixels")
# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()
time.sleep(1)

print("show Hello World")
display.fill(0)
display.text('Hello', 0, 0, 1)
display.text('World', 0, 10, 1)
display.show()
time.sleep(2)

print("show random stars")

for _ in range(10):
    for _ in range(50):
        x = random.randrange(width)
        y = random.randrange(height)
        display.pixel(x, y, 1)
    display.show()
    display.fill(0)

print("done.")
time.sleep(0)
