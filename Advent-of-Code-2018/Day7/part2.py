import collections
import string

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

print(res)

steps = []

for line in res:
    steps.append((line.split()[1],line.split()[7]))
    
sortedsteps = sorted(steps, key=lambda x: (x[0], x[1]))

pathDict = collections.OrderedDict()
for tup in sortedsteps:
    pathDict[tup[0]] = []
    pathDict[tup[1]] = []

for tup in sortedsteps:
    try:
        pathDict[tup[1]].append(tup[0])
    except KeyError:
        pass

ordering = []
secondstack = []
mainstack = []

letters = list(string.ascii_uppercase)
#worktime = 60 + index(letters[i]) + 1

for k,v in pathDict.items():
    if pathDict[k] == []:
        mainstack.append(k)
print(mainstack)
while mainstack:
    mainstack = sorted(mainstack)
    fulfill = mainstack.pop(0)
    print("popping" + str(fulfill))
    ordering.append(fulfill)
    for k,v in pathDict.items():
        try:
            pathDict[k].remove(fulfill)
        except:
            pass
    for k,v in pathDict.items():
        if pathDict[k] == [] and k not in ordering and k not in mainstack:
            mainstack.append(k)
    #secondstack = sorted(secondstack)
    #print(secondstack)
    #for item in secondstack:
    #    mainstack.append(item)
    #secondstack = []
    print(pathDict)

print(''.join(ordering))
