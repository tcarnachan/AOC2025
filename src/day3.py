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