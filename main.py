#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime, timedelta, date
import time


CALENDAR_ID = "CALENDAR_ID"
CALENDAR_KEY = "CALENDAR_TOKEN"
TELEGRAM_TOKEN = "TELEGRAM_TOKEN"
TELEGRAM_CID= "TELEGRAM_CHAT_ID"



names = {}


time_calendar = datetime.utcnow() - timedelta(days=1)
time_tomorrow = datetime.utcnow() 
time_calendar = time_calendar.strftime('%Y-%m-%dT23:59:59.59-01:00')
time_tomorrow = time_tomorrow.strftime('%Y-%m-%dT00:00:00.00-01:00')



url = "https://content.googleapis.com/calendar/v3/calendars/"+CALENDAR_ID+"/events?singleEvents=true&orderBy=startTime&timeMin="+str(time_calendar)+"&timeMax="+str(time_tomorrow)+"&key="+CALENDAR_KEY
print(url)

r = requests.get(url)
open('eventos.json', 'wb').write(r.content)
f = open('eventos.json', encoding="utf-8")
json_file = json.load(f)
json_str = json.dumps(json_file).encode('utf8')
resp = json.loads(json_str)
events = json_str.decode().count("summary") -1
print(events)


if (events <= 0):
	print("NO HAY CUMPLEAÑOS HOY")
else:
	for i in range (events):
		names[i] = resp['items'][i]['summary']
		try:
			requests.post('https://api.telegram.org/bot'+TELEGRAM_TOKEN+'/sendMessage', data={'chat_id': TELEGRAM_CID , 'text': "Hoy es el cumpleaños de  "+names[i]+"."}) 
		except:
			requests.post('https://api.telegram.org/bot'+TELEGRAM_TOKEN+'/sendMessage', data={'chat_id': TELEGRAM_CID , 'text': "Ha ocurrido un error"})  



