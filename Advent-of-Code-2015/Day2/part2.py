
with open('input.txt', 'r') as f:
    data = f.read()
    res = [i for i in data.splitlines()]
# feet of ribbon is smallest face perimeter plus cubic feet of volume

total_ribbon = 0
for line in res:
    dimensions = line.split("x")
    l, w, h = dimensions
    l, w, h = int(l), int(w), int(h)
    perimeter = min(2*l+2*w, 2*w+2*h, 2*h+2*l)
    volume = l*w*h
    total_ribbon += perimeter + volume

print(total_ribbon)
#print(res)