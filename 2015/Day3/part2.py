with open('input.txt', 'r') as f:
    data = f.read()
    #res = [i for i in data.splitlines()]

#print(data)
first = data[::2]
second = data[1::2]

print(first)
print(second)

x1 = 0
y1 = 0
x2 = 0
y2 = 0

presents = {
    (0, 0):2
}

for char in first:
    if char == ">":
        x1 += 1
    elif char == "<":
        x1 -= 1
    elif char == "^":
        y1 += 1
    elif char == "v":
        y1 -= 1
    try:
        presents[(x1, y1)] += 1
    except KeyError:
        presents[(x1, y1)] = 1

for char in second:
    if char == ">":
        x2 += 1
    elif char == "<":
        x2 -= 1
    elif char == "^":
        y2 += 1
    elif char == "v":
        y2 -= 1
    try:
        presents[(x2, y2)] += 1
    except KeyError:
        presents[(x2, y2)] = 1

print(len(presents))