with open('input.txt', 'r') as f:
    data = f.read()
    #res = [i for i in data.splitlines()]

#print(data)

x = 0
y = 0

presents = {
    (0, 0):1
}
print(presents)
for char in data:
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y += 1
    elif char == "v":
        y -= 1
    try:
        presents[(x, y)] += 1
    except KeyError:
        presents[(x, y)] = 1
print(presents)
print(len(presents))