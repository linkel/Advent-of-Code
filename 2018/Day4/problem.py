import os
import numpy
from dateutil.parser import parse
import datetime

with open('input.txt', 'r') as f:
    data = f.read()
res = [str(i) for i in data.splitlines()]
date = []
for item in res:
    date.append(item.split())
compiled = []
for item in date:
    firsthalf = item[0]
    secondhalf = item[1]
    one_date = firsthalf[1:] + " " + secondhalf[0:-1]
    if "begins" in item:
        action = item[3][1:]
    elif "wakes" in item:
        action = "wakes"
    elif "falls" in item:
        action = "sleeps"
    compiled.append([one_date, action])
#1518-07-2600:24
#['1518-11-22 23:59', '3109'], ['1518-11-23 00:21', 'sleeps']
sorted_compiled = sorted(compiled, key=lambda x: datetime.datetime.strptime(x[0],'%Y-%m-%d %H:%M'))

guards = {}
only73 = []
for item in sorted_compiled:
    nap = 0
    if item[1] != "wakes" and item[1] != "sleeps":
        current_guard = item[1]
    elif item[1] == "sleeps":
        start_sleep = parse(item[0])
    elif item[1] == "wakes":
        nap = parse(item[0]) - start_sleep
    if nap != 0:
        try:
            guards[current_guard] += (nap.seconds // 60 % 60)
        except KeyError:
            guards[current_guard] = (nap.seconds // 60 % 60)
    if current_guard == "73":
        only73.append(item)

mins = {}
minute_start = None
minute_end = None
for item in only73:
    if item[1] == "sleeps":
        minute_start = int(item[0][14:]) #parse(item[0]).seconds // 60 % 60
    elif item[1] == "wakes":
        minute_end = int(item[0][14:]) #parse(item[0]).seconds // 60 % 60
    if minute_start != None and minute_end != None:
        for i in range(minute_start,minute_end):
            try:
                mins[i] += 1
            except KeyError:
                mins[i] = 1

#print(max(guards.values()))
print(max(mins.values()))