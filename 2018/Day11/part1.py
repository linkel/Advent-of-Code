import collections
import matplotlib.pyplot as plt
from blist import blist
import numpy

INPUT = 9221


def findPower(X,Y,INP):
    rackID = X+10
    startlvl = rackID*Y
    nextlvl = startlvl + INP
    nextlvl = nextlvl * rackID
    hundredths = str(nextlvl)[-3]
    hundredths = int(hundredths)
    final = hundredths - 5
    return final

#print(findPower(122,79,57))

grid = numpy.zeros((300, 300))

#for (x,y), value in numpy.ndenumerate(grid):
#    print(x,y)

for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        grid[y][x] = findPower(x+1,y+1,INPUT)

sumNine = []
current_largest_num = 0
current_coords = None
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        examining = []
        for subsetx in range(x, x+3):
            for subsety in range(y, y+3):
                try:
                    examining.append(grid[subsety][subsetx])
                except:
                    pass
        print(len(examining))
        if len(examining) == 9:
            print(sum(examining))
            if sum(examining) > current_largest_num:
                current_largest_num = sum(examining)
                current_coords = (x+1,y+1)

print(current_coords)
print(current_largest_num)
print(grid)
plt.imshow(grid, cmap="gray")
plt.show()