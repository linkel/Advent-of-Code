import os
import numpy
from dateutil.parser import parse
import datetime
import string

with open('input.txt', 'r') as f:
    data = f.read()
    res = list(data)
    #res = [str(i) for i in data.splitlines()]

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

print(res)
print(len(res))

i = 0
j = 1
while i != (len(res)-1):
    char = res[i]
    try:
        char2 = res[j]
    except KeyError:
        break
    try:
        idx = lowercase.index(char) 
        if char2 == uppercase[idx]:
            del res[j]
            del res[i]
            i=0
            j=1
            print("pair deleted 1")
    except ValueError:
        idx = uppercase.index(char) 
        if char2 == uppercase[idx]:
            del res[j]
            del res[i]
            i=0
            j=1
            print("pair deleted 2")
    i += 1
    j += 1
    print(len(res))
print(res)
print(len(res))