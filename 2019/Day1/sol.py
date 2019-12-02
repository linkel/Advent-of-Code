import os

with open('input.txt', 'r') as f:
    data = f.read()

def part1():
    vals = [int(i) for i in data.split()]

    accum = 0

    for val in vals:
        accum += val // 3 - 2

    print(accum)

vals = [int(i) for i in data.split()]

def part2(vals):
    accum = 0

    for val in vals:
        sub_res = 0
        val = val // 3 - 2
        while val > 0:
            sub_res += val
            val = val // 3 - 2
        accum += sub_res
    print(accum)

testy = [100756]

part2(testy)
part2(vals)

