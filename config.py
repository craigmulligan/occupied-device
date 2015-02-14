import os

# CONFIG
fbRef = os.getenv('FIREBASE')
twilio_acc_id = os.getenv('TWILIO_ACC_ID')
twilio_acc_auth_token = os.getenv('TWILIO_ACC_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')

keen.project_id = os.getenv('KEEN_PROJ_ID')
keen.write_key = os.getenv('KEEN_WRITE_KEY')
keen.read_key = os.getenv('KEEN_READ_KEY')
keen.master_key = os.getenv('KEEN_MASTER_KEY')