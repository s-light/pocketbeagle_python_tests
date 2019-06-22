#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for apds9960 sensor in combination with ssd1306 oled.

    requires:
    adafruit-circuitpython-apds9960
    adafruit-circuitpython-ssd1306
"""

import time

import board
import busio
import digitalio

import adafruit_apds9960.apds9960
import adafruit_ssd1306
BitmapFont = adafruit_ssd1306.framebuf.BitmapFont()

print("combined test with apds9960 and ssd1306 oled display")

print("setup i2c & spi & digitalio")
i2c = busio.I2C(board.SCL, board.SDA)
spi = busio.SPI(board.SCLK, board.MOSI)
pin_cs = digitalio.DigitalInOut(board.P2_6)
pin_rst = digitalio.DigitalInOut(board.P1_2)
pin_dc = digitalio.DigitalInOut(board.P1_4)

print("setup APDS9960")
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

print("init SSD1306_SPI")
width = 128
height = 64
# width, height, spi, dc, reset, cs
display = adafruit_ssd1306.SSD1306_SPI(
    width, height, spi, pin_dc, pin_rst, pin_cs)


# ------------------------------------------
gesture_name = {
    0: "No",
    1: "Up",
    2: "Down",
    3: "Left",
    4: "Right",
}

text_positions = {
    'gesture': (0, 0),
    'proximity': (0, 0),
    'color': (0, 0),
}


# ------------------------------------------
def display_text(text, pos):
    """Display text and return end position."""
    x, y = pos
    scale = 1
    display.text(text, x, y, scale)
    width = BitmapFont.width(text)
    return x + width


# ------------------------------------------

def setup_sensor():
    """Prepare Sensor."""
    print("setup Sensor")
    sensor.enable_proximity = True
    sensor.enable_gesture = True
    sensor.enable_color = True


def setup_display():
    """Prepare Display."""
    print("setup Display")
    display.fill(0)
    display.show()
    line_height = BitmapFont.font_height + 2

    # gesture
    temp_x = 0
    temp_y = 0 * line_height
    temp_x = display_text('gesture: ', (temp_x, temp_y))
    text_positions['gesture'] = (temp_x, temp_y)
    display_text('-', text_positions['gesture'])
    # proximity
    temp_x = 0
    temp_y = 1 * line_height
    temp_x = display_text('proximity: ', (temp_x, temp_y))
    text_positions['proximity'] = (temp_x, temp_y)
    display_text('-', text_positions['proximity'])
    # color
    temp_x = 0
    temp_y = 2 * line_height
    temp_x = display_text('color: ', (temp_x, temp_y))
    text_positions['color'] = (temp_x, temp_y)
    display_text('-', text_positions['color'])

    display.show()


def update_gesture(gesture):
    """Update Gesture."""
    # print('Saw gesture: {}: {}'.format(gesture, gesture_name[gesture]))
    display_text('    ', text_positions['gesture'])
    display_text(gesture_name[gesture], text_positions['gesture'])


def update_proximity(proximity):
    """Update proximity."""
    display_text('    ', text_positions['proximity'])
    display_text(proximity, text_positions['proximity'])


def update_color(color_data):
    """Update Color."""
    r, g, b, c = color_data
    format_string = 'r: {}, g: {}, b: {}, c: {}'
    # print(format_string.format(r, g, b, c))
    display_text(format_string.format(r, g, b, c), text_positions['color'])


# ------------------------------------------

def main():
    """Main."""
    setup_sensor()
    setup_display()
    print("Main Loop")
    gesture = 0
    proximity = 0
    color = 0
    flag_mod = False
    try:
        while True:
            flag_mod = False
            gesture_new = sensor.gesture()
            if gesture_new is not 0:
                if gesture is not gesture_new:
                    gesture = gesture_new
                    update_gesture(gesture)
                    flag_mod = True
            proximity_new = sensor.proximity()
            if proximity is not proximity_new:
                proximity = proximity_new
                update_proximity(proximity)
                flag_mod = True
            color_new = sensor.color_data
            if color is not color_new:
                color = color_new
                update_color(color)
                flag_mod = True
            if flag_mod:
                display.show()
    except KeyboardInterrupt as e:
        print('exit')


if __name__ == '__main__':
    main()
