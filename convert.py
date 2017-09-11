#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
soup=False
# with open("example.html", encoding='utf-8') as f:
# 	INPUT=f.read()

import requests
url = input("Enter URL with auth info (http://user:password@website.com/plany/plan.html):")
INPUT = requests.get(url).text
OUTPUT=""
table=BeautifulSoup(INPUT,"html.parser").find_all("table",class_="tabela")[0]

columns_extract=[]

schedule=[]
day=0
for row in table.find_all("tr"):
	schedule.append([])
	for item in row.find_all("th"):
		columns_extract.append(item.get_text())
		pass
	for item in row.find_all("td"):
		schedule[day].append(item.get_text())
		pass
	day=day+1
	pass

columns={}

for column in range(len(columns_extract)):
	columns[column]=[]
	for i in range(len(schedule)):
		for ii in range(len(schedule[i])):
			if ii == column:
				columns[column].append(schedule[i][ii])

from icalendar import Calendar,Event
from datetime import datetime, date, timedelta

today = datetime.today().replace(hour=0,minute=0,second=0,microsecond=0)

import calendar
hours={}

nearest_monday = today+timedelta(days=(-today.weekday()))

for x in range(0,len(columns[0])):
	time=columns[1][x]
	start=time.split("-")[0]
	end=time.split("-")[1]
	starttime=int(start.split(":")[0])*60+int(start.split(":")[1])
	endtime=int(end.split(":")[0])*60+int(end.split(":")[1])
	hours[x]=[starttime,endtime]
	pass

cal = Calendar()

day=None
for day in range(2,len(columns)):
	actual_day=nearest_monday+timedelta(days=(day-2))
	for a in range(0,len(columns[day])):
		if columns[day][a] != '\xa0':
			event = Event()
			event.add('summary', columns[day][a])
			event.add('dtstart', actual_day+timedelta(minutes=hours[a][0]))
			event.add('dtend', actual_day+timedelta(minutes=hours[a][1]))
			event.add("rrule",{"FREQ":"DAILY","INTERVAL":7})
			cal.add_component(event)
		pass
	pass

	# friday is 6
	# monday is 2

with open("schedule.ical","wb") as f:
	f.write(cal.to_ical())
