from collections import namedtuple

with open('res/day10.txt') as f:
    lines = f.read().splitlines()

Machine = namedtuple("Machine", ["indicator", "schematics", "joltage_reqs"])

machines = []
for line in lines:
    split = line.split()
    machines.append(Machine(
        split[0][1:-1],
        [[int(s) for s in sch[1:-1].split(',')] for sch in split[1:-1]],
        [int(r) for r in split[-1][1:-1].split(',')]
    ))

total = 0
for machine in machines:
    paths = set(["." * len(machine.indicator)])
    while not any(
        all(x == y for x, y in zip(machine.indicator, p)) for p in paths
    ):
        next = set()
        for p in paths:
            for sch in machine.schematics:
                tmp = list(p)
                for button in sch:
                    tmp[button] = { '.': '#', '#': '.' }[tmp[button]]
                next.add("".join(tmp))
        paths = next
        total += 1
print(f"Part 1: {total}")