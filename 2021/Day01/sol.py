lines = [int(line.rstrip()) for line in open("input", "r")]
print(lines)

res = 0 
for i in range(len(lines)-1):
    if lines[i+1] > lines[i]:
        res += 1

print(res)
