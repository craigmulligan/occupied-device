#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import time
from firebase import firebase
import occupiedo

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	 
while True:
	input_state = GPIO.input(17)
	fb_state = occupiedo.check_door()
	state = occupiedo.binarize(fb_state)
	print "input_state: " + str(input_state)
	print "fb_state: " + str(state)
	#check if physical doors input is the same as firebase if not - update firebase
	if state != input_state:
		#door state has changed so fire off actions
		occupiedo.change_occupied_state(fb_state)
	time.sleep(0.2)