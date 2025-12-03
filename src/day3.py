with open("res/day3.txt") as f:
    j = f.read().split('\n')

def get_joltage(num_on):
    total = 0
    for line in j:
        line_total = ""
        for digits_left in range(num_on, 0, -1):
            line_total += max(line[:1 + len(line) - digits_left])
            line = line[line.index(line_total[-1]) + 1:]
        total += int(line_total)
    return total

# Part 1
print("Part 1:", get_joltage(2))

# Part 2
print("Part 2:", get_joltage(12))

# Golf - 134 chars
print([sum((int(''.join([(p:=l.index(max(l[p:1+len(l)-n+d]),p)+1,l[p-1])[1]for d in range(n)])))for l in j if~(p:=0))for n in[2,12]])