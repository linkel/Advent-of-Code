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
square_tuples = []
square_tuples = blist(square_tuples)
for i in range(0, 300):
    print(i)
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            examining = []
            for subsetx in range(x, x+i):
                for subsety in range(y, y+i):
                    try:
                        examining.append(grid[subsety][subsetx])
                    except:
                        pass
            if sum(examining) > current_largest_num:
                current_largest_num = sum(examining)
                current_coords = (x+1,y+1)
                square_tuples.append((current_largest_num, current_coords, i))
    print(sorted(square_tuples, key=lambda x: x[0]))

#print(current_coords)
#print(current_largest_num)
#print(grid)
#plt.imshow(grid, cmap="gray")
#plt.show()

print(square_tuples)
#print(sorted(square_tuples))
print(sorted(square_tuples, key=lambda x: x[0]))