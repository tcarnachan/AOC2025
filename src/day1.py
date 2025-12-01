with open("res/day1.txt") as f:
    inp = f.read().split('\n')

curr = 50
count1, count2 = 0, 0
for i, dir in enumerate(inp):
    rot = int(dir[1:])
    if dir[0] == 'L': curr = (100 - curr) % 100
    d, curr = divmod(curr + rot, 100)
    count2 += d
    if curr == 0: count1 += 1
    if dir[0] == 'L': curr = (100 - curr) % 100
    
print("Part 1:", count1)
print("Part 2:", count2)