#!/usr/bin/env python3


import requests
import urllib.request
from bs4 import BeautifulSoup
import time
import os
import datetime
import json

path = os.getcwd()

if os.path.exists(f'{path}/Horoscopes') == False:
    os.mkdir(f'{path}/Horoscopes')

os.chdir(f'{path}/Horoscopes')


#gets today's date
currenttime = datetime.datetime.now()
date = currenttime.strftime('%Y-%m-%d')

signs = ['aries','taurus','gemini','cancer','leo','virgo','libra',
          'scorpio','sagittarius','capricorn','aquarius','pisces']

# check to see if a json file already exists with previous days horoscopes
try:
    file = open('horoscopes.json','r')
    horoscopes = json.load(file)
    file.close()

# if the file isn't found, create a new variable
except FileNotFoundError:
    horoscopes = {}
    newfile = True


for sign in signs:

    res = requests.get(f'https://www.astrology.com/horoscope/daily/{sign}.html')
    soupObj = BeautifulSoup(res.text,'html.parser')

    #Get text
    dailyText = soupObj.find('p')
    output = dailyText.get_text()

    #remove date tag
    index = output.find(': ')
    description = output[(index+2):len(output)]

    if newfile == True:
        horoscopes[sign] = {date:description}

    else:
        horoscopes[sign].update({date:description})

    time.sleep(1)

# dumps the json object to a string
Jhoroscopes = json.dumps(horoscopes)

file = open('horoscopes.json','w')
file.write(Jhoroscopes)
file.close()

print('Complete')
