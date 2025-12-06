import math

with open('res/day6.txt') as f:
    raw_lines = f.read().splitlines()
    lines = [l.split() for l in raw_lines]

operations = [sum if op == '+' else math.prod for op in lines[-1]]

# Part 1
operands = []
for col in range(len(lines[0])):
    operands.append([int(row[col]) for row in lines[:-1]])
print(sum([op(nums) for op, nums in zip(operations, operands)]))

# Part 2
operands = [[]]
for col in range(len(raw_lines[0])):
    num = ''.join([row[col] for row in raw_lines[:-1]]).strip()
    if len(num) == 0: operands.append([])
    else: operands[-1].append(int(num))
print(sum([op(nums) for op, nums in zip(operations, operands)]))