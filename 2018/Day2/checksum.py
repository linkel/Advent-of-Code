import os

with open('input.txt', 'r') as f:
    data = f.read()

res = [str(i) for i in data.split()]

hasThrees = 0
hasTwos = 0

for item in res:
    myDict = {}
    hasThree = False
    hasTwo = False
    for char in item:
        try:
            myDict[char] += 1
        except KeyError:
            myDict[char] = 1
    for k,v in myDict.items():
        if v == 3:
            hasThree = True
        if v == 2:
            hasTwo = True
    if hasThree == True:
        hasThrees += 1
    if hasTwo == True:
        hasTwos += 1

print(hasThrees)
print(hasTwos)
print(hasThrees * hasTwos)
