#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    simple test for SPI adafruit-BBIO.

    https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/spi
"""

from Adafruit_BBIO.SPI import SPI
#spi = SPI(bus, device) #/dev/spidev<bus>.<device>

# /dev/spidev0.0
spi = SPI(1, 0)
print(spi.xfer2([32, 11, 110, 22, 220]))
spi.close()

print("Hello BBIO SPI!")
