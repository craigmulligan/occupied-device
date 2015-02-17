#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import time
from firebase import firebase
import occupiedo

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
prev_state = 0;

# TODO: use multi thread interupts instead of loop.	 
while True:
	input_state = GPIO.input(17)
	print "input_state: " + str(input_state)
	print "prev_state: " + str(prev_state)
	#check if physical doors input is the same as firebase if not - update firebase
	if input_state != prev_state:
		#door state has changed so fire off actions
		occupiedo.change_occupied_state(input_state)

	prev_state = input_state
	time.sleep(0.2)