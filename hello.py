#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import time
from firebase import firebase
import occupiedo

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	 
while True:
    input_state = GPIO.input(17)
    if input_state == False:
		print('Button Pressed')
		current_state = occupiedo.check_door()
		occupiedo.change_occupied_state(current_state)
		time.sleep(0.2)