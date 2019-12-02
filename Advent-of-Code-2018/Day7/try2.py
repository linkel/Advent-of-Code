import collections

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

print(res)

steps = []

for line in res:
    steps.append((line.split()[1],line.split()[7]))
    
sortedsteps = sorted(steps, key=lambda x: (x[0], x[1]))
for i in sortedsteps:
    print(i)
#print(sortedsteps)

class TreeNode:
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children # an array of child items

for i in sortedsteps:
    