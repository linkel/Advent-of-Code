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

import networkx
Graph = networkx.DiGraph()

NEITHER, CLIMBING, TORCH = 0, 1, 2

def equipment(erosion_level):
    terrain = erosion_level % 3
    if terrain == ROCKY:
        return {CLIMBING, TORCH}
    if terrain == WET:
        return {NEITHER, CLIMBING}
    if terrain == NARROW:
        return {NEITHER, TORCH}

for y in range(len(grid)):
    for x in range(len(grid[0])):
        equippable = equipment(grid[y][x])
        for tool1 in equippable:
            for tool2 in equippable:
                if tool1 == tool2:
                    continue
                Graph.add_edge((x,y,tool1),(x,y,tool2), weight=7)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        for neighborX, neighborY in [(x-1, y),(x+1, y),(x, y-1),(x, y+1)]:
            if neighborX < 0 or neighborX >= len(grid[0]):
                continue
            if neighborY < 0 or neighborY >= len(grid):
                continue
            current = grid[y][x]
            destination = grid[neighborY][neighborX]
            tools = equipment(current).intersection(equipment(destination))
            for tool in tools:
                Graph.add_edge((x,y,tool),(neighborX,neighborY,tool),weight=1)

shortest_route_path = networkx.dijkstra_path(Graph, (0, 0, 2), (targetX, targetY, 2))
shortest_route = networkx.dijkstra_path_length(Graph, (0, 0, 2), (targetX, targetY, 2))

print(shortest_route_path)
print(shortest_route)