import collections
import matplotlib.pyplot as plt
from blist import blist

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]
#'position=< 9,  1> velocity=< 0,  2>'
print(res)


class Point(object):
    def __init__(self, posX, posY, velX, velY):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        self.updateCycle = 0
    def update(self):
        self.posX += self.velX
        self.posY += self.velY 
        self.updateCycle += 1

#def

points = []
points = blist(points)

for s in res:
    position = s[s.find("<")+1:s.find(">")]
    velocity = s[s.rfind("<")+1:s.rfind(">")]
    position = [int(i) for i in position.split(",")]
    velocity = [int(i) for i in velocity.split(",")]
    combo = position + velocity
    points.append(Point(combo[0], combo[1], combo[2], combo[3]))


for i in range(10400):
    xcoord = []
    xcoord = blist(xcoord)
    ycoord = []
    ycoord = blist(ycoord)
    for point in points:
        xcoord.append(point.posX)
        ycoord.append(point.posY)
        point.update()
for i in range(2000):
    print(i)
    xcoord = []
    xcoord = blist(xcoord)
    ycoord = []
    ycoord = blist(ycoord)
    for point in points:
        xcoord.append(point.posX)
        ycoord.append(point.posY)
        point.update()
    plt.plot(xcoord, ycoord, color='r', marker=".",linestyle='None')
    plt.show()
