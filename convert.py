#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event

url = input("Enter URL with auth info (ex: http://user:password@website.com/path_to/schedule.html):\n")
response = requests.get(url).text
table = BeautifulSoup(response, "html.parser").find_all("table", class_="tabela")[0]

columns_extract = []

schedule = []
day = 0
for row in table.find_all("tr"):
    schedule.append([])
    for item in row.find_all("th"):
        columns_extract.append(item.get_text())

    for item in row.find_all("td"):
        schedule[day].append(item.get_text())

    day = day + 1

columns = {}

for column in range(len(columns_extract)):
    columns[column] = []
    for i in range(len(schedule)):
        for ii in range(len(schedule[i])):
            if ii == column:
                columns[column].append(schedule[i][ii])

today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
nearest_monday = today + timedelta(days=(-today.weekday()))

hours = {}
for x in range(0, len(columns[0])):
    time = columns[1][x]
    start = time.split("-")[0]
    end = time.split("-")[1]
    starttime = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    endtime = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
    hours[x] = [starttime, endtime]


cal = Calendar()
day = None
for day in range(2, len(columns)):
    actual_day = nearest_monday + timedelta(days=(day - 2))
    for a in range(0, len(columns[day])):
        if columns[day][a] != '\xa0':
            event = Event()
            event.add('summary', columns[day][a])
            event.add('dtstart', actual_day + timedelta(minutes=hours[a][0]))
            event.add('dtend', actual_day + timedelta(minutes=hours[a][1]))
            event.add("rrule", {"FREQ": "DAILY", "INTERVAL": 7})
            cal.add_component(event)

# friday is 6
# monday is 2

with open("schedule.ical", "wb") as f:
    f.write(cal.to_ical())
