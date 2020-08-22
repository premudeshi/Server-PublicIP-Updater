from twilio.rest import Client
from config import *
from requests import get

ip = get('https://api.ipify.org').text


#print(sid)

text = 'Your IP is ' + str(ip)

account_sid = sid
auth_token = auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=froms,
    body=text,
    to=tos
)

print(message.sid)


#file = open('publicip.txt', 'w+')

