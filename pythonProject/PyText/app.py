from email import message
from http import client
from pydoc import cli
from twilio.rest import Client

account_sid = "_Insert Acct SID_"
auth_token = "_Insert Auth Token_"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to='_Insert Phone Number_',
    from_='_Insert Phone Number_',
    body="This messsage was sent out using Ben's code in python, wohoo!"
)

print(call.sid)
