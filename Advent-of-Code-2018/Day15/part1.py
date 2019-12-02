import collections
import matplotlib.pyplot as plt
from blist import blist
import numpy as np
np.set_printoptions(threshold=np.nan)
np.set_printoptions(linewidth=140)

with open('example4.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

# len of res is 32 x and y

grid = np.empty((32,32), dtype="U")
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

#print(grid)

wall, clear = "#", "."
width, height = 32, 32

def bfsForElf(grid, start, goal):
    queue = collections.deque([[start]])
    seen = set([start])
    allPaths = []
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            allPaths.append(path)
        for x2, y2 in ((x,y-1),(x-1,y),(x+1,y),(x,y+1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and grid[y2][x2] != "E" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    for path in allPaths:
        for goblin in goblinList:
            if (goblin.posX, goblin.posY) == path[-1]:
                return path

def bfsForGoblin(grid, start, goal):
    queue = collections.deque([[start]])
    seen = set([start])
    allPaths = []
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            allPaths.append(path)
        for x2, y2 in ((x,y-1),(x-1,y),(x+1,y),(x,y+1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and grid[y2][x2] != "G" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    for path in allPaths:
        for elf in elfList:
            if (elf.posX, elf.posY) == path[-1]:
                return path

class Elf(object):
    def __init__(self, posY, posX):
        self.who = "E"
        self.posY = posY
        self.posX = posX
        self.attackPower = 3
        self.hp = 200
    def findTarget(self):
        grid[self.posY][self.posX] = "F"
        path = bfsForElf(grid, (self.posX, self.posY), "G")
        grid[self.posY][self.posX] = "E"
        if path == None:
            pass
        #    if grid[self.posY-1][self.posX] == '.':
        #        grid[self.posY][self.posX] = "."
        #        self.posY -= 1
        #        grid[self.posY][self.posX] = "E"
        elif len(path) > 2:
            grid[self.posY][self.posX] = "."
            elfNextTo = False
            for elf in elfList:
                if (elf.posX,elf.posY) == path[1]:
                    print("can't move")
                    elfNextTo = True
            if elfNextTo == False:
                self.posX = path[1][0]
                self.posY = path[1][1]
            grid[self.posY][self.posX] = "E"
            goblinList.sort(key=lambda x: (x.hp))
            for goblin in goblinList:
                 if ((goblin.posX, goblin.posY) == (self.posX - 1, self.posY)) or ((goblin.posX, goblin.posY) == (self.posX + 1, self.posY)) or ((goblin.posX, goblin.posY) == (self.posX, self.posY + 1)) or ((goblin.posX, goblin.posY) == (self.posX, self.posY - 1)):
                     self.attack(goblin)
                     goblinList.sort(key=lambda x: (x.posY,x.posX))
                     break
        elif len(path) == 2:
            goblinList.sort(key=lambda x: (x.hp))
            for goblin in goblinList:
                 if ((goblin.posX, goblin.posY) == (self.posX - 1, self.posY)) or ((goblin.posX, goblin.posY) == (self.posX + 1, self.posY)) or ((goblin.posX, goblin.posY) == (self.posX, self.posY + 1)) or ((goblin.posX, goblin.posY) == (self.posX, self.posY - 1)):
                     self.attack(goblin)
                     goblinList.sort(key=lambda x: (x.posY,x.posX))
                     break
            #for goblin in goblinList:
            #    if goblin.posX == path[1][0] and goblin.posY == path[1][1]:
            #        self.attack(goblin)
            #        break
    def attack(self, target):
        target.hp = target.hp - self.attackPower
        if target.hp < 1:
            grid[target.posY][target.posX] = "."
            goblinList.remove(target)
            alltogetherList.remove(target)


class Goblin(object):
    def __init__(self, posY, posX):
        self.who = "G"
        self.posY = posY
        self.posX = posX
        self.attackPower = 3
        self.hp = 200
    def findTarget(self):
        grid[self.posY][self.posX] = "H"
        path = bfsForGoblin(grid, (self.posX, self.posY), "E")
        grid[self.posY][self.posX] = "G"
        if path == None:
            #for elf in elfList:
            #    if ((elf.posX, elf.posY) == (self.posX - 1, self.posY)) or ((elf.posX, elf.posY) == (self.posX + 1, self.posY)) or ((elf.posX, elf.posY) == (self.posX, self.posY + 1)) or ((elf.posX, elf.posY) == (self.posX, self.posY - 1)):
            #        self.attack(elf)
            #        break
            
        elif len(path) > 2:
            grid[self.posY][self.posX] = "."
            gobNextTo = False
            for goblin in goblinList:
                if (goblin.posX,goblin.posY) == path[1]:
                    print("can't move")
                    gobNextTo = True
            if gobNextTo == False:
                self.posX = path[1][0]
                self.posY = path[1][1]
            self.posX = path[1][0]
            self.posY = path[1][1]
            grid[self.posY][self.posX] = "G"
            elfList.sort(key=lambda x: (x.hp))
            for elf in elfList:
                 if ((elf.posX, elf.posY) == (self.posX - 1, self.posY)) or ((elf.posX, elf.posY) == (self.posX + 1, self.posY)) or ((elf.posX, elf.posY) == (self.posX, self.posY + 1)) or ((elf.posX, elf.posY) == (self.posX, self.posY - 1)):
                     self.attack(elf)
                     elfList.sort(key=lambda x: (x.posY,x.posX))
                     break
        elif len(path) == 2:
            elfList.sort(key=lambda x: (x.hp))
            for elf in elfList:
                 if ((elf.posX, elf.posY) == (self.posX - 1, self.posY)) or ((elf.posX, elf.posY) == (self.posX + 1, self.posY)) or ((elf.posX, elf.posY) == (self.posX, self.posY + 1)) or ((elf.posX, elf.posY) == (self.posX, self.posY - 1)):
                     self.attack(elf)
                     elfList.sort(key=lambda x: (x.posY,x.posX))
                     break
            #for elf in elfList:
            #    if elf.posX == path[1][0] and elf.posY == path[1][1]:
            #        self.attack(elf)
            #        break
    def attack(self, target):
        target.hp = target.hp - self.attackPower
        if target.hp < 1:
            grid[target.posY][target.posX] = "."
            elfList.remove(target)
            alltogetherList.remove(target)

goblinList = []
elfList = []

for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if grid[y][x] == "G":
            goblinList.append(Goblin(y,x))
        elif grid[y][x] == "E":
            elfList.append(Elf(y,x))

alltogetherList = goblinList + elfList
alltogetherList.sort(key=lambda x: (x.posY,x.posX))
roundd = 0
while len(goblinList) > 0 and len(elfList) > 0:
    for elf in elfList:
        print(elf.hp)
    for goblin in goblinList:
        print(goblin.hp)
    for fighter in alltogetherList:
        if len(goblinList) == 0 or len(elfList) == 0:
            print("fighters killed before round end")
            roundd -= 1
            break
        fighter.findTarget()
    alltogetherList.sort(key=lambda x: (x.posY,x.posX))
    goblinList.sort(key=lambda x: (x.posY,x.posX))
    elfList.sort(key=lambda x: (x.posY,x.posX))
    #for y in range(grid.shape[0]):
    #    for x in range(grid.shape[1]):
    #        if grid[y][x] == "G":
    #            grid[y][x] = "."
    #        elif grid[y][x] == "E":
    #            grid[y][x] = "."
    #for fighter in alltogetherList:
    #    grid[fighter.posY][fighter.posX] = fighter.who
    print(grid)
    roundd += 1
    print(roundd)

print(elfList)
print(goblinList)
sumhp = 0
for goblin in goblinList:
    sumhp += goblin.hp
print("goblinhp")
print(sumhp)
print("round num")
print(roundd)

elfhps = 0
for elf in elfList:
    elfhps += elf.hp

print("elf hps")
print(elfhps)