#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import time
from firebase import firebase
import occupiedo

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	 
while True:
    input_state = GPIO.input(17)
    if input_state == True:
		print('Button Pressed')
		current_state = occupiedo.check_door()
		#check if physical doors input is the same as firebase if not - update firebase
		if current_state != input_state:
			#door state has changed so fire off actions
			occupiedo.change_occupied_state(current_state)
		time.sleep(0.2)