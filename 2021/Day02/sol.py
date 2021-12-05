lines = [line.rstrip() for line in open("input", "r")]
print(lines)

fwd = "forward"
up = "up"
down = "down"

directions = {
    fwd: (0, 1),
    up: (-1, 0),
    down: (1, 0)
}

horizontal = 0
depth = 0

for line in lines:
    tup = line.split()
    direction = tup[0]
    value = int(tup[1])
    depth += directions[direction][0] * value
    horizontal += directions[direction][1] * value

print(horizontal, depth)
print(horizontal * depth)
