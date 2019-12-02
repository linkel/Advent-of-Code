DEPTH = 11820
TEST_DEPTH = 510
TARGET = (7,782)
TEST_TARGET = (10,10)

#geologic index at 0,0 and at target is 0
# if Y is 0, geo index is X*16807
# if X is 0, geo index is Y*48271
# else multiply erosion levels of regions at x-1,y and x,y-1

#erosion level is geo index plus depth modulo 20183
# then erosion level modulo 3, if 0 is rocky, if 1 is wet,
# if 2, is narrow

ROCKY, WET, NARROW = 0, 1, 2

targetX, targetY = TARGET

grid = []
for y in range(targetY+50):
    row = []
    for x in range(targetX+50):
        row.append(0)
    grid.append(row)

for y in range(targetY+50):
    for x in range(targetX+50):
        if x == 0 and y == 0:
            geo = 0
        elif x == 0:
            geo = y*48271
        elif y == 0:
            geo = x*16807
        elif targetX == x and targetY == y:
            geo = 0
        else:
            geo = grid[y-1][x] * grid[y][x-1]
        erosion = (geo + DEPTH) % 20183
        grid[y][x] = erosion

summ = 0
for y in range(targetY + 1):
    for x in range(targetX + 1):
        summ += grid[y][x] % 3
print(summ)

