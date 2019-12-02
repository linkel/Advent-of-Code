import os

with open('input.txt', 'r') as f:
    data = f.read()

res = [int(i) for i in data.split()]

start_sum = 0
dictionary = {}
checker = False
while res:
    for item in res:
        try:
            if dictionary[start_sum] == 1:
                print(start_sum)
                checker = True
                break
        except KeyError:
            dictionary[start_sum] = 1
        start_sum += item
    if checker == True:
        break
#print(start_sum)

