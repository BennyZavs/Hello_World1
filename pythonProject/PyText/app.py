from email import message
from http import client
from pydoc import cli
from twilio.rest import Client

account_sid = "ACd6f696870ade2c4d9d4e927213539754"
auth_token = "5c869801e8dc67ad7e15d1c80ad51bd3"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to='4706097040',
    from_='8596511817',
    body="This messsage was sent out using Ben's code in python, wohoo!"
)

print(call.sid)
