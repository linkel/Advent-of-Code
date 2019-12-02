import collections

with open('input.txt', 'r') as f:
    data = f.read()

res = [int(i) for i in data.split()]

print(res)



class Node:
    def __init__(self, childs=[], metadata=[]):
        self.childs = childs
        self.metadata = metadata

metasum = 0

def sumMeta(alist):
    childs = alist[:2][0]
    metadata = alist[:2][1]
    alist = alist[2:]
    mySum = 0

    for i in range(childs):
        total, alist = sumMeta(alist)
        mySum += total

    mySum += sum(alist[:metadata])

    return (mySum, alist[metadata:])



#total, remaining = sumMeta(res)

#print('answer for metadata totals:', total)




def values(alist):
    childs = alist[:2][0]
    metadata = alist[:2][1]
    alist = alist[2:]
    numbers = []
    mySum = 0

    for i in range(childs):
        total, number, alist = values(alist)
        mySum += total
        numbers.append(number) # store these to sum together later

    mySum += sum(alist[:metadata])

    if childs == 0:
        return (mySum, sum(alist[:metadata]), alist[metadata:])
    else:
        toAdd = []
        for num in alist[:metadata]:
            if num > 0 and num <= len(numbers):
                toAdd.append(numbers[num-1])
        tempsum = sum(toAdd)
        return (
            mySum,
            tempsum,
            alist[metadata:]
        )

total, value, remaining = values(res)

print('part 2:', value)