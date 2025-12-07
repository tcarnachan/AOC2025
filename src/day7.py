from collections import defaultdict

with open('res/day7.txt') as f:
    lines = f.read().splitlines()

curr = { lines[0].index('S'): 1 }
splits = set()
for row in range(1, len(lines)):
    new = defaultdict(int)
    for col, count in curr.items():
        if lines[row][col] == '.':
            new[col] += count
        elif lines[row][col] == '^':
            splits.add((row, col))
            if col - 1 >= 0:
                new[col - 1] += count
            if col  + 1 < len(lines[0]):
                new[col + 1] += count
    curr = new

print(f"Part 1: {len(splits)}")
print(f"Part 2: {sum(curr.values())}")