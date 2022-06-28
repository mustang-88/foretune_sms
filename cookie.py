import pandas as pd
import numpy as np
import bs4
import os.path
import time
from bs4 import BeautifulSoup #, NavigableString, Tag
import re
import requests
import json
import time



def cookie():
    url = 'http://www.fortunecookiemessage.com/'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    category = soup.findAll("div", attrs={"class": "quote"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("a", attrs={"class": "cookie-link"})

    # Head values (COlumn names) are the first items of the body list
    # header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    # return the header names of the columns in the first row
    fortune = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            fortune.append(var)

    # headers.pop(0)
    # fortune = fortune[0].text

    # Return the fortune
    return fortune


# name the variable that will house the output from the website
fortune = cookie()

# remove list properties
fortune = fortune[0]

#print(fortune)