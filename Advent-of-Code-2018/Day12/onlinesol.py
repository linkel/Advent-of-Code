initial_state = None
rules = {}
with open('input.txt', 'r') as fp:
    for line in fp:
        if not initial_state:
            initial_state = line.split()[2]
        elif len(line) > 1:
            parts = line.split()
            rules[parts[0]] = parts[2]

print(rules)
prefix = "........."
state =  prefix + str(initial_state) + ".................."
index_offset = len(prefix)
segment_length = 5
generations = 100
def score(state):
    total = 0
    for i in range(0, len(state)):
        if state[i] == "#":
            total += (i - index_offset)
    return total

scores = []
for g in range(0, generations):
    next_state = "...."
    for i in range(2, len(state) - segment_length):
        segment = state[i:i+segment_length]
        if segment in rules:
            next_state += rules[segment]
            if i == (len(state) - segment_length) - 1:
                next_state += "."
        else:
            next_state += "."
    next_state += "..."
    
    state = next_state
    scores.append(score(state))

print(state)

diffs = [scores[i+1]-scores[i] for i in range(len(scores)-1)]
for i in range(0, len(scores)-1):
    print(str(i) + " " + str(scores[i]) + " " + str(diffs[i]) + " " + str(((i - 89) * 15) + 2047))

print((((50000000000-1) - 89) * 15) + 2047)