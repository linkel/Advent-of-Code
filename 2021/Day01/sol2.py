lines = [int(line.rstrip()) for line in open("input", "r")]
print(lines)

res = 0 
for i in range(len(lines)-3):
    s = lines[i] + lines[i+1] + lines[i+2]
    nxt = lines[i+1] + lines[i+2] + lines[i+3]
    if nxt > s:
        res += 1

print(res)
