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

myList = []

print(res)
print(len(res))
originalres = res[:]

for l in range(len(lowercase)):
    i = 0
    j = 1
    res = originalres[:]
    while i != (len(res)-1):
        char = res[i]
        if lowercase[l] == char:
            del res[i]
            i = i - 1
        elif uppercase[l] == char:
            del res[i]
            i = i - 1
        i = i + 1
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
                i = i - 4
                j = j - 4
                print("pair deleted 1")
        except ValueError:
            try:
                idx = uppercase.index(char) 
                if char2 == lowercase[idx]:
                    del res[j]
                    del res[i]
                    i = i - 4
                    j = j - 4
                    print("pair deleted 2")
            except ValueError:
                pass
        i += 1
        j += 1
        print(len(res))
    #print(res)
    print("LETTER " + lowercase[l])
    print(len(res))
    myList.append((len(res)))

print(min(myList))
