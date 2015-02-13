import os
from firebase import firebase
import requests
from twilio.rest import TwilioRestClient
from config import fbRef, twilio_acc_id, twilio_acc_auth_token, twilio_number

FIREBASE = firebase.FirebaseApplication(fbRef, None)

# Checks the current state of door firebase
def check_door(): 
	url = fbRef + '.json?orderBy="$key"&limitToFirst=1&print=pretty'
	data = requests.get(url)
	json_object = data.json()
	status = json_object['OCCUPIED']
	if status == "true":
		return "false"
	else: 
		return "true"

# updates firebase to the new state
def change_occupied_state(state):
	result = FIREBASE.put('/', 'OCCUPIED', state)
	# only send text if toilet is open
	if state == "false":
		get_next_in_queue()

# sends text to next in queue
def send_text(number, name):
	# Your Account Sid and Auth Token from twilio.com/user/account
	client = TwilioRestClient(twilio_acc_id, twilio_acc_auth_token)
	message = client.messages.create(body=name + " the toilet is now open!",
	    to= number,    # Replace with your phone number
	    from_=twilio_number) # Replace with your Twilio number
	print "text sent"

def binarize(fb_state): 
	if fb_state == "true":
		return 1
	else:
		return 0

# gets next in queue
def get_next_in_queue():
	url = fbRef +'queue.json?orderBy="$key"&limitToFirst=1&print=pretty'
	data = requests.get(url)
	json_object = data.json()
	person = None
	number = None

	# get lastest entry
	for key in json_object: 
		person = json_object[key]
	
	# check if anyone is in queue
	if person == None:
		print "no one in queue"
	else:
		name = person['name']
		number = os.getenv(name, '+447479559980')
		# send text
		send_text(number, name)
		# delete entry
		FIREBASE.delete('/queue', key)