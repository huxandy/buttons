#!/usr/bin/env python
#
# buttons
# Control your pi with Gpio
# Use a switch or a motion detector
#
# Author : Sarrailh Remi
# Copyright : Gplv3
#

import sys
import threading
import time

from lib import Commands
from lib import TriggersINI

#Check if it is a Raspberry Pi or an orange Pi
raspberrypi = True

for line in open("/proc/cpuinfo"):
    if "sun8i" in line:
        raspberrypi = False

if raspberrypi:
    from lib import Gpio
    import RPi.GPIO as GPIO
else:
    from lib import Gpio_h3 as Gpio

# Commands.send("printenv")
configurationFile = "/opt/user/config/buttons/buttons.cfg"
sys.stdout.write("GPIO Triggers ON\n")

# Get triggers from configuration file
triggers = TriggersINI.openConfiguration(configurationFile)
if triggers is not False:
    sys.stdout.write("Configuration: " + configurationFile + "\n")
else:
    sys.stdout.write("Configuration: " + configurationFile + " failed to load\n")
    sys.exit(1)

sys.stdout.write("Collector: gpio\n")
sys.stdout.write("--------------------------\n")
sys.stdout.write("waiting for IO...\n")
sys.stdout.write("To exit press [Ctrl-C]\n")

ButtonsThread = threading.Thread(target=Gpio.Buttons, args=(triggers,))
ButtonsThread.daemon = True
ButtonsThread.start()
try:
    while True:
        buttonPressed = Gpio.getState()
        action = TriggersINI.checkTrigger(triggers, buttonPressed)
        # print action
        if action is not False:
            sys.stdout.write("GPIO: "+buttonPressed+"\n")
            sys.stdout.write("\n")
            sys.stdout.write("COMMAND: "+action+"\n")
            sys.stdout.write("-------------\n")
            Commands.send(action)

        buttonPressed = False
        time.sleep(0.020)
except KeyboardInterrupt:
    sys.stdout.write("-----------------------\n")
    sys.stdout.write("GPIO Triggers OFF\n")
    if raspberrypi:
        GPIO.cleanup()
