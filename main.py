import publicip
from twilio.rest import Client


print(publicip.get())

file = open('publicip.txt', 'w+')

