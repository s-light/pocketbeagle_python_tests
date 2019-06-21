#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test for PWM frequency."""

import board
import pulseio

##########################################
print(42 * '*')
print("test for pwm frequency")

freqency = (6000 * 1000)  # 6MHz
pwm = pulseio.PWMOut(
    board.P2_36,
    duty_cycle=(2 ** 15),
    frequency=freqency,
    variable_frequency=True)
print("pwm.frequency: {:}MHz".format(pwm.frequency / (1000*1000)))

##########################################
# main loop
print(42 * '*')
print("loop")

print("you can change the pwm.frequency:")
print("new frequency in MHz: ")
while True:
    new_value = input()
    new_freq_Hz = pwm.frequency
    try:
        new_freq_Hz = int(float(new_value) * 1000 * 1000)
    except Exception as e:
        print("Exception: ", e)
    print(
        "calculated frequency: {:}MHz (= {:}Hz)".format(
            new_freq_Hz / (1000*1000),
            new_freq_Hz
        )
    )
    pwm.frequency = new_freq_Hz
    # reset duty_cycle to half
    # https://circuitpython.readthedocs.io/en/latest/shared-bindings/pulseio/PWMOut.html#pulseio.PWMOut.duty_cycle
    pwm.duty_cycle = 0x7fff
    # pwm.duty_cycle = (2 ** 15)
    print("pwm.frequency: {:}MHz".format(pwm.frequency / (1000*1000)))
    # prepare new input
    print("\nenter new frequency in MHz: ")
