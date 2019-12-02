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
only863 = []
only3203 = []
only3109 = []
only2833 = []
only3373 = []
only191 = []
only1811 = []
only2677 = []
only3391 = []
only79 = []
only2347 = []
only1217 =[]
only1061=[]
only1789=[]
only3313=[]
only479=[]
only709=[]
only3331=[]
only2591=[]
only1579=[]
only1951=[]
only2371=[]


guardlist = []
for item in sorted_compiled:
    nap = 0
    if item[1] != "wakes" and item[1] != "sleeps":
        current_guard = item[1]
        guardlist.append(item[1])
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
    elif current_guard == "863":
        only863.append(item)
    elif current_guard == "3203":
        only3203.append(item)
    elif current_guard == "3109":
        only3109.append(item)
    elif current_guard == "2833":
        only2833.append(item)
    elif current_guard == "3373":
        only3373.append(item)
    elif current_guard == "191":
        only191.append(item)
    elif current_guard == "1811":
        only1811.append(item)
    elif current_guard == "2677":
        only2677.append(item)
    elif current_guard == "3391":
        only3391.append(item)
    elif current_guard == "2347":
        only2347.append(item)
    elif current_guard == "79":
        only79.append(item)        
    elif current_guard == "1217":
        only1217.append(item)
    elif current_guard == "1061":
        only1061.append(item)
    elif current_guard == "1789":
        only1789.append(item)
    elif current_guard == "3313":
        only3313.append(item)
    elif current_guard == "479":
        only479.append(item)
    elif current_guard == "709":
        only709.append(item)
    elif current_guard == "3331":
        only3331.append(item)
    elif current_guard == "2591":
        only2591.append(item)
    elif current_guard == "1579":
        only1579.append(item)
    elif current_guard == "1951":
        only1951.append(item)
    elif current_guard == "2371":
        only2371.append(item)

#guardlistset = set(guardlist)
#print(guardlistset)


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
print(73)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only863:
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
print(863)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only3203:
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
#print(3203)
#print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only3109:
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
print(3109)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only2833:
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
print(2833)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only3373:
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
print(3373)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only191:
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
print(191)
print(max(mins.items(), key=lambda k: k[1]))

mins = {}
minute_start = None
minute_end = None
for item in only1811:
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
print(1811)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only2677:
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
print(2677)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only3391:
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
print(3391)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only79:
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
print(79)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only2347:
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
print(2347)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only1217:
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
print(1217)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only1061:
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
print(1061)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only1789:
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
print(1789)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only3313:
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
print(3313)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only479:
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
#print(479)

#print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only709:
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
print(709)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only3331:
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
#print(3331)
#print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only2591:
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
print(2591)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only1579:
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
print(1579)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only1951:
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
print(1951)
print(max(mins.values()))

mins = {}
minute_start = None
minute_end = None
for item in only2371:
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
print(2371)
print(max(mins.values()))