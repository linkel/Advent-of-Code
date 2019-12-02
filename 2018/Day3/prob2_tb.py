import os
import numpy
import matplotlib.pyplot as plt
 


with open('input.txt', 'r') as f:
    data = f.read()
quilt = numpy.zeros((1000,1000))
res = [str(i) for i in data.splitlines()]
for item in res:
    xy = item.split()[2][0:-1]
    x = int(xy.split(",")[0])
    y = int(xy.split(",")[1])
    size = item.split()[3]
    width = int(size.split("x")[0])
    height = int(size.split("x")[1])
    quilt[y:y+height,x:x+width] += 1
for item in res:
    xy = item.split()[2][0:-1]
    x = int(xy.split(",")[0])
    y = int(xy.split(",")[1])
    size = item.split()[3]
    width = int(size.split("x")[0])
    height = int(size.split("x")[1])
    checker = False
    if numpy.all(quilt[y:y+height,x:x+width] == 1):
        checker = True
    if checker == True:
        print(item)


unique, counts = numpy.unique(quilt, return_counts=True)
print(dict(zip(unique, counts)))
#['#1026', '@', '838,675:', '23x18']

plt.imshow(quilt, cmap="gray")
plt.show()