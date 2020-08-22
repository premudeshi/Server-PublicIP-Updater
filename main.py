import publicip
from twilio.rest import Client
from config import *


print(sid)

print(publicip.get())

file = open('publicip.txt', 'w+')

