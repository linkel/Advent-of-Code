import collections
import matplotlib.pyplot as plt
from blist import blist
import numpy as np

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

print(len(res))
#length 150
grid = np.empty((151,151), dtype="U")
y=0
x=0
# generate map
for line in res:
    #print(line)
    x=0
    for char in line:
        #print(char)
        #print(x)
        grid[y][x] = char
        x += 1
    y += 1

class Cart(object):
    def __init__(self, posY, posX, direction, underneath):
        self.facings = ["<","^",">","v"]
        self.posY = posY
        self.posX = posX
        self.direction = direction
        self.turns = 0
        self.updateCycle = 0
        self.underneath = underneath
    def decideDir(self):
        if self.turns == 0:
            #turn left
            try:
                self.direction = self.facings[self.facings.index(self.direction) - 1]
            except IndexError:
                self.direction = self.facings[-1]
            self.turns += 1
        elif self.turns == 1:
            #go straight
            self.turns += 1
        elif self.turns == 2:
            #turn right
            try:
                self.direction = self.facings[self.facings.index(self.direction) + 1]
            except IndexError:
                self.direction = self.facings[0]
            self.turns = 0
    def update(self):
        if self.direction == "<":
            self.posX -= 1
        elif self.direction == "^":
            self.posY -= 1
        elif self.direction == ">":
            self.posX += 1
        elif self.direction == "v":
            self.posY += 1
        # I want to run update first, then if it hits a + then decide direction
        self.updateCycle += 1

carts = [] #sort them??
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if grid[y][x] == "<" or grid[y][x] == ">":
            carts.append(Cart(y,x,grid[y][x],"-"))
            # removing carts off map for ease?
            grid[y][x] = "-"
        elif grid[y][x] == "^" or grid[y][x] == "v":
            carts.append(Cart(y,x,grid[y][x],"|"))
            grid[y][x] = "|"

def checkCollision(alistofCarts):
    compare = {}
    for cart in alistofCarts:
        try:
            if compare[(cart.posX,cart.posY)] != cart:
                print("COLLISION")
                print((cart.posX, cart.posY))
                #print(cart.updateCycle)
                carts.remove(compare[(cart.posX,cart.posY)])
                print(compare[(cart.posX,cart.posY)])
                carts.remove(cart)
                print(cart)
                compare.pop((cart.posX,cart.posY))
        except KeyError:
            compare[(cart.posX,cart.posY)] = cart
    return 0

while len(carts) != 1:
    carts.sort(key=lambda x: (x.posY,x.posX))
    #for cart in carts:
    #    print((cart.posY, cart.posX))
    for cart in carts:
        cart.update()
        checkCollision(carts)
        #print((cart.posX, cart.posY))
        if grid[cart.posY][cart.posX] == "\\":
            if cart.direction == "<":
                cart.direction = "^"
            elif cart.direction == "v":
                cart.direction = ">"
            elif cart.direction == ">":
                cart.direction = "v"
            elif cart.direction == "^":
                cart.direction = "<"
        elif grid[cart.posY][cart.posX] == "/":
            if cart.direction == ">":
                cart.direction = "^"
            elif cart.direction == "v":
                cart.direction = "<"
            elif cart.direction == "<":
                cart.direction = "v"
            elif cart.direction == "^":
                cart.direction = ">"
        elif grid[cart.posY][cart.posX] == "+":
            cart.decideDir()
            #grid[cart.posY][cart.posX] = cart.underneath

print(carts)
print((carts[0].posX,carts[0].posY))

#Collision at 37 136
#Collision at 39 98
#Collision at 3 138
#Collision at 69 134
#Collision at 104 41
#Collision at 106 118
#Collision at 50 93
#Collision at 64 53
#Last Cart: 53,112
