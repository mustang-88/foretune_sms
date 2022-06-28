from cookie import fortune
from datetime import datetime
import time
import pandas as pd
import numpy as np
import os


def datalog():
    # file_path = (os.chdir("C:\\Users\\John\\Desktop\\Apps\\sms\\log.csv"))
    while not os.path.exists("C:\\Users\\John\\Desktop\\Apps\\sms\\log.csv"):
        time.sleep(6)
        today = datetime.now()
        df = pd.DataFrame(columns=["Date", "Fortune"])
        df["Date"] = pd.Series(today)
        df["Fortune"] = pd.Series(fortune)
        df.to_csv("log.csv")

    if os.path.isfile("C:\\Users\\John\\Desktop\\Apps\\sms\\log.csv"):
        df = pd.read_csv("log.csv")
        time.sleep(6)
        today = datetime.now()
        df["Date"].append(pd.Series(today), ignore_index=True)
        df["Fortune"].append(pd.Series(fortune), ignore_index=True)
        df.to_csv("log.csv")
    else:
        raise ValueError("%s isn't a file!" % "C:\\Users\\John\\Desktop\\Apps\\sms\\log.csv")

        return df


datalog = datalog()