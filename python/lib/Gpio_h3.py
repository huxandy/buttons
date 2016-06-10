#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv

from pyA20.gpio import gpio as GPIO
from pyA20.gpio import port
import time


global buttonPressed
buttonPressed = False

h3pin = { 
    2:12,
    3:11,
    4:6,
    17:1,
    27:0,
    22:3,
    10:64,
    9:65,
    11:66,
    0:19,
    5:7,
    6:8,
    13:9,
    19:10,
    26:20,
    14:13,
    15:14,
    18:110,
    23:68,
    24:71,
    25:2,
    8:67,
    7:21,
    1:18,
    12:200,
    16:201,
    20:198,
    21:199
}

pipin = dict((v, k) for k, v in h3pin.iteritems())

def Buttons(triggers):
    buttons = triggers.sections()
    GPIO.init()
    pins = []
    gpioType = []
    i = 0
    for button in buttons:
        gpioType.append(button[0])
        pins.append(h3pin[int(button[1:])])
        if gpioType[i] == "B":
            GPIO.setcfg(pins[i], GPIO.INPUT)
            GPIO.pullup(pins[i], GPIO.PULLUP)
        if gpioType[i] == "M":
            GPIO.setcfg(pins[i], GPIO.INPUT)
        i = i + 1

    global buttonPressed
    while True:
        i = 0
        for pin in pins:
            if gpioType[i] == "B":
                if not GPIO.input(pin):
                    buttonPressed = "B" + str(pipin[pin])
            if gpioType[i] == "M":
                if GPIO.input(pin):
                    buttonPressed = "M" + str(pipin[pin])
            i = i + 1
        time.sleep(0.020)


def getState():
    global buttonPressed
    state = buttonPressed
    buttonPressed = False
    return state
