from collections import namedtuple
from ortools.linear_solver import pywraplp
import numpy as np

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

total = 0
for machine in machines:
    A = []
    for button in machine.schematics:
        row = [0 for _ in machine.joltage_reqs]
        for b in button: row[b] = 1
        A.append(row)
    
    A = np.array(A)
    b = np.array(machine.joltage_reqs)

    m, n = A.shape

    solver = pywraplp.Solver.CreateSolver("CBC")
    x = [solver.IntVar(0, solver.infinity(), f"x[{i}]") for i in range(m)]
    for row in range(n):
        solver.Add(sum(A[col, row] * x[col] for col in range(m)) == b[row])
    solver.Minimize(solver.Sum(x))

    solver.Solve()

    total += sum([int(v.solution_value()) for v in x])
print(f"Part 2: {total}")