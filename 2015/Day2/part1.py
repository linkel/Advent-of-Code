
with open('input.txt', 'r') as f:
    data = f.read()
    res = [i for i in data.splitlines()]

total_paper = 0
for line in res:
    dimensions = line.split("x")
    l, w, h = dimensions
    l, w, h = int(l), int(w), int(h)
    slack = min([l*w,w*h,h*l])
    surface_area = 2*l*w + 2*w*h + 2*h*l
    total_paper += slack + surface_area

print(total_paper)
#print(res)