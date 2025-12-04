with open("res/day1.txt") as f:
    s = f.read().split('\n')

curr, curr_dir = 50, 'R'
count1, count2 = 0, 0
for dir in s:
    if dir[0] != curr_dir:
        curr = (100 - curr) % 100
        curr_dir = dir[0]
    d, curr = divmod(curr + int(dir[1:]), 100)
    count1 += int(curr == 0)
    count2 += d
    
print("Part 1:", count1)
print("Part 2:", count2)

# Golf - 127 chars
d,r,o,t,h=50,'R',0,0,100
print(*map(sum,zip(*[(t+(d:=(d if r==(r:=i[0])else(h-d)%h)+int(i[1:]))//h,o+(d:=d%h)==0)for i in s])))

# That prints it as 'part2 part1', to print part1 first costs an extra 7 characters
print(*map(sum,zip(*[(o+(d:=(d if r==(r:=i[0])else(h-d)%h)+int(i[1:]))%h==0,t+(d,d:=d%h)[0]//h)for i in s])))