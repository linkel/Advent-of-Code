import os
import numpy as np
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]
print(res)

newHold = []
for line in res:
    newHold.append((tuple(int(i) for i in line.split(', '))))
print(newHold)
mapper = np.zeros((400,400))

#plt.scatter(*zip(*newHold))
#plt.show()

for i, tup in enumerate(newHold):
    x = tup[0]
    y = tup[1]
    if mapper[y][x] == 0:
        mapper[y][x] = i

plt.imshow(mapper, cmap="viridis")
plt.show()