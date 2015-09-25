#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv

import RPi.GPIO as GPIO
import time


global buttonPressed
buttonPressed = False


def Buttons(triggers):
    buttons = triggers.sections()
    GPIO.setmode(GPIO.BCM)
    pins = []
    gpioType = []
    i = 0
    for button in buttons:
        gpioType.append(button[0])
        pins.append(int(button[1:]))
        if gpioType[i] == "B":
            GPIO.setup(pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if gpioType[i] == "M":
            GPIO.setup(pins[i], GPIO.IN)
        i = i + 1

    global buttonPressed
    while True:
        i = 0
        for pin in pins:
            if gpioType[i] == "B":
                if not GPIO.input(pin):
                    buttonPressed = "B" + str(pin)
            if gpioType[i] == "M":
                if GPIO.input(pin):
                    buttonPressed = "M" + str(pin)
            i = i + 1
        time.sleep(0.020)


def getState():
    global buttonPressed
    state = buttonPressed
    buttonPressed = False
    return state
