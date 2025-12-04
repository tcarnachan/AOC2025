from itertools import product

with open("res/day4.txt") as f:
    grid = f.read().split('\n')

def access_rolls(grid):
    accessible = []
    for rix, row in enumerate(grid):
        for cix, item in enumerate(row):
            if item == '.': continue
            adj = 0
            for r, c in product(range(rix - 1, rix + 2), range(cix - 1, cix + 2)):
                if (r != rix or c != cix) and 0 <= r < len(grid) \
                        and 0 <= c < len(row) and grid[r][c] == '@':
                    adj += 1
            if adj < 4: accessible.append((rix, cix))
    return accessible

# Part 1
print(len(access_rolls(grid)))

# Part 2
total = 0
grid_list = [list(row) for row in grid]
while len(accessible := access_rolls(grid_list)) > 0:
    for (r, c) in accessible:
        grid_list[r][c] = '.'
    total += len(accessible)
print(total)