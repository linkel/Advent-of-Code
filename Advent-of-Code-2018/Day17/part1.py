import collections
import matplotlib.pyplot as plt
from blist import blist
import numpy as np 

np.set_printoptions(threshold=np.nan)
np.set_printoptions(linewidth=140)

with open('testrun.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

print(res)

grid = np.empty((15,600), dtype="U")
grid.fill(".")
grid[0][500] = "+"
for section in res:
    #print(section.split(","))
    if section[0] == "x":
        xandy = section.split(",")
        x = int(xandy[0][2:])
        #print(x)
        yrange = xandy[1][3:]
        yrange = yrange.split("..")
        #print(yrange)
        for y in range(int(yrange[0]),int(yrange[1])+1):
            grid[y][x] = "#"
    elif section[0] == "y":
        xandy = section.split(",")
        y = int(xandy[0][2:])
        #print(x)
        xrang = xandy[1][3:]
        xrang = xrang.split("..")
        #print(xrang)
        for x in range(int(xrang[0]),int(xrang[1])+1):
            grid[y][x] = "#"


class MovingWater(object):
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.update = 0
        self.direction = "down"
    def flow(self):
        if self.direction = "down":
            if grid[self.posY+1][self.posX] == ".":
                self.posY += 1
                grid[self.posY][self.posX] = "|"
            else:
                xspread = 0
                while grid[self.posY][self.posX+xspread] != "#" and grid[self.posY][self.posX+xspread] != "~":
                    grid[self.posY][self.posX+xspread] = "~"
                    xspread += 1
                    print("looping")
                xspread = 1
                while grid[self.posY][self.posX-xspread] != "#" and grid[self.posY][self.posX-xspread] != "~":
                    grid[self.posY][self.posX-xspread] = "~"
                    xspread += 1
                self.sideflowed = True:
        elif self.direction = "up":


        self.update += 1


new = MovingWater(500,0)
for i in range(10):
    new.flow()

e = grid[:,494:508]
print(e)
