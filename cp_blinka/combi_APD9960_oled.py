#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simple test for apds9960 sensor in combination with ssd1306 oled.

    requires:
    adafruit-circuitpython-apds9960
    adafruit-circuitpython-ssd1306
"""

import time
import datetime

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
    "gesture": (0, 0),
    "proximity": (0, 0),
    "color": (0, 0),
    "red": (0, 0),
    "green": (0, 0),
    "blue": (0, 0),
    "clear": (0, 0),
}


# ------------------------------------------
def clear_text(text, pos):
    """Clear area for text."""
    x, y = pos
    color = 0
    width = BitmapFont.width(text)
    height = BitmapFont.font_height
    display.fill_rect(x, y, width, height, color)
    return x + width


def display_text(text, pos):
    """Display text and return end position."""
    x, y = pos
    color = 1
    width = BitmapFont.width(text)
    display.text(text, x, y, color)
    return x + width


# ------------------------------------------

def setup_sensor():
    """Prepare Sensor."""
    print("setup Sensor")
    sensor.enable_proximity = True
    sensor.enable_gesture = True
    # sensor.enable_color = True


def setup_display():
    """Prepare Display."""
    print("setup Display")
    display.fill(0)
    display.show()
    line_height = BitmapFont.font_height + 2

    # gesture
    temp_x = 0
    temp_y = 0 * line_height
    temp_x = display_text("gesture: ", (temp_x, temp_y))
    text_positions["gesture"] = (temp_x, temp_y)
    display_text("-", text_positions["gesture"])
    # proximity
    temp_x = 0
    temp_y = 1 * line_height
    temp_x = display_text("proximity: ", (temp_x, temp_y))
    text_positions["proximity"] = (temp_x, temp_y)
    display_text("-", text_positions["proximity"])
    # color
    # temp_x = 0
    # temp_y = 2 * line_height
    # temp_x = display_text("red: ", (temp_x, temp_y))
    # text_positions["red"] = (temp_x, temp_y)
    # temp_x = 0
    # temp_y = 3 * line_height
    # temp_x = display_text("green: ", (temp_x, temp_y))
    # text_positions["green"] = (temp_x, temp_y)
    # temp_x = 0
    # temp_y = 4 * line_height
    # temp_x = display_text("blue: ", (temp_x, temp_y))
    # text_positions["blue"] = (temp_x, temp_y)
    # temp_x = 0
    # temp_y = 5 * line_height
    # temp_x = display_text("clear: ", (temp_x, temp_y))
    # text_positions["clear"] = (temp_x, temp_y)

    display.show()


# ------------------------------------------

def update_gesture(gesture):
    """Update Gesture."""
    # print("Saw gesture: {}: {}".format(gesture, gesture_name[gesture]))
    clear_text("mmmmm", text_positions["gesture"])
    display_text(gesture_name[gesture], text_positions["gesture"])


def update_proximity(proximity):
    """Update proximity."""
    format_string = "{: >4}"
    clear_text(format_string.format(proximity), text_positions["proximity"])
    display_text(format_string.format(proximity), text_positions["proximity"])


def update_color(color_data):
    """Update Color."""
    red, green, blue, clear = color_data
    # format_string = "r: {: >4}, g: {: >4}, b: {: >4}, c: {: >4}"
    # print(format_string.format(r, g, b, c))
    # display_text(format_string.format(r, g, b, c), text_positions["color"])
    format_string = "{: >4}"
    clear_text(format_string.format(red), text_positions["red"])
    display_text(format_string.format(red), text_positions["red"])
    clear_text(format_string.format(green), text_positions["green"])
    display_text(format_string.format(green), text_positions["green"])
    clear_text(format_string.format(blue), text_positions["blue"])
    display_text(format_string.format(blue), text_positions["blue"])
    clear_text(format_string.format(clear), text_positions["clear"])
    display_text(format_string.format(clear), text_positions["clear"])


# ------------------------------------------

def main():
    """Main."""
    setup_sensor()
    setup_display()
    print("Main Loop")
    print("-----")
    gesture_last = None
    proximity_last = None
    color_last = (0, 0, 0, 0)
    gesture = 0
    proximity = None
    color = (0, 0, 0, 0)
    flag_mod = False
    try:
        while True:
            # flag_mod = False
            gesture = sensor.gesture()
            # if gesture is not 0:
            if gesture != gesture_last:
                # print("\n gesture update")
                gesture_last = gesture
                update_gesture(gesture)
                # flag_mod = True
                display.show()
            # proximity = sensor.proximity()
            # if proximity != proximity_last:
            #     # print("\n proximity update")
            #     proximity_last = proximity
            #     update_proximity(proximity)
            #     flag_mod = True
            # color = sensor.color_data
            # if color != color_last:
            #     color_last = color
            #     update_color(color)
            #     flag_mod = True
            # if flag_mod:
            #     display.show()
            print(
                "{} "
                "gesture: {: >5};  "
                # "proximity: {: >4};  "
                # "color: {: >4} {: >4} {: >4} {: >4};  "
                "".format(
                    datetime.datetime.now(),
                    gesture_name[gesture],
                    # proximity,
                    # *color
                ),
                end="\r"
            )
            time.sleep(0.0001)
    except KeyboardInterrupt as e:
        print("\n  → exit")
    finally:
        display.fill(0)
        display.show()


if __name__ == "__main__":
    main()
