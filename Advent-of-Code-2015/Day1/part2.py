
with open('input.txt', 'r') as f:
    data = f.read()
    
floor = 0

for num, char in enumerate(data):
    if char == "(": floor += 1  
    else: floor += -1
    if floor == -1:
        print(num + 1)
        break

#print(floor)