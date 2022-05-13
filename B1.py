import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid,auth_token)

 #crt_msg = client.messages.create(
 #    to= "",
 #    from_ ="+18106414934",
 #    body= "Hello Rashmi you gotta sleep now",
 #)

# print("Created a new message {}".format(crt_msg.sid))

for msg in client.messages.list():
    print(msg)
    print(msg.body)