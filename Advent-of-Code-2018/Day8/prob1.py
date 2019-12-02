import collections

with open('ex.txt', 'r') as f:
    data = f.read()

res = [int(i) for i in data.split()]

print(res)



class Node:
    def __init__(self, childs=[], metadata=[]):
        self.childs = childs
        self.metadata = metadata

metasum = 0

def sumMeta(alist):
    metasum = 0
    try:
        howManyChild = alist[0]
        howManyMeta = alist[1]
    except IndexError:
        return metasum
    if howManyChild == 0:
        if howManyMeta > 0:
            metasum += sum(alist[2:2+howManyMeta])
            return sumMeta(alist[2+howManyMeta:])
        elif howManyMeta == 0:
            return 0
    else:
        metasum += sumMeta(alist[2:])
    return metasum

    
    #else:
        #metasum += sumMeta(alist[2:2+howManyMeta])
    #metasum += sumMeta(alist[2+howManyMeta:])
    #metasum += sum(alist[])

print(sumMeta(res))