import os
from decimal import Decimal
import os
import pandas as pd
import numpy as np
from twilio.rest import Client
from logger import datalog
from cookie import fortune
from cookie import fortune
from twilio.rest import Client

fortune
datalog
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACd7de5fb3e00fb7145b67a66d0d760279"
auth_token = "7757cf6b23f3da9f53648f60920eaa02"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body= fortune,
         from_='+15072487536',
         to='+19173655936'
     )

#print(message.sid)