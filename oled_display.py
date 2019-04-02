#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    simple test for adafruit-circuitpython-ssd1306.

    based on
    https://learn.adafruit.com/adafruit-oled-featherwing/circuitpython-and-python-usage#full-example-code-8-40
"""

import board
import digitalio
import busio

import adafruit_ssd1306

spi = busio.SPI(board.SCLK, board.MOSI)
pin_cs = digitalio.DigitalInOut(board.P2_6)
pin_rst = digitalio.DigitalInOut(board.P1_2)
pin_dc = digitalio.DigitalInOut(board.P1_4)

# width, height, spi, dc, reset, cs
display = adafruit_ssd1306.SSD1306_SPI(128, 32, spi, pin_dc, pin_rst, pin_cs)

print("oled display tests")

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

print("should be blank ;-)")

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()
