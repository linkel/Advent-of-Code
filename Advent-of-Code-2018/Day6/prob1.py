import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

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

rows = mapper.shape[0]
cols = mapper.shape[1]

for num, top in enumerate(newHold):
    first = list(newHold[num])
    for i in range(0, rows):
        for j in range(0, cols):
            if ((mapper[i][j] > distance.cityblock(first, [i,j])) or (mapper[i][j] == 0)):
                mapper[i][j] = distance.cityblock(first, [i,j])
            elif mapper[i][j] == distance.cityblock(first, [i,j]):
                mapper[i][j] = -1000
    print(num)
    plt.imshow(mapper, cmap="viridis")
    plt.show()

plt.imshow(mapper, cmap="viridis")
plt.show()