with open('res/day9.txt') as f:
    lines = [l.split(',') for l in f.read().splitlines()]

coords = [(int(x), int(y)) for x, y in lines]

# Part 1
def calc_area(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)

rect_areas = []
for i, c1 in enumerate(coords):
    for c2 in coords[i + 1:]:
        rect_areas.append((c1, c2, calc_area(c1, c2)))
rect_areas.sort(key=lambda r: r[2], reverse=True)
print(f"Part 1: {rect_areas[0][2]}")