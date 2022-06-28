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
account_sid = "AccountSID"
auth_token = "AuthToken"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body= fortune,
         from_='+Your_Number',
         to='+External_Cel'
     )

#print(message.sid)
