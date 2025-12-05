with open("res/day5.txt") as f:
    id_range, id_available = map(str.splitlines, f.read().split("\n\n"))

ranges = [list(map(int, r.split("-"))) for r in id_range]

# Part 1
count = 0
for id in id_available:
    count += any(start <= int(id) <= end for start, end in ranges)
print(count)

# Part 2
ranges.sort(key=lambda x: x[0])
merged = [ranges[0]]
for start, end in ranges[1:]:
    curr = merged[-1]
    if start > curr[1]: merged.append([start, end])
    elif end >= curr[1]: merged[-1][1] = end
print(sum([end - start + 1 for start, end in merged]))