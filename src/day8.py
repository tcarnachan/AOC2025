from collections import defaultdict
from math import prod

with open('res/day8.txt') as f:
    lines = f.read().splitlines()

coords = []
for line in lines:
    x, y, z = map(int, line.split(','))
    coords.append((x, y, z))

sqr_dists = []
for i, e1 in enumerate(coords):
    (x1, y1, z1) = e1
    for e2 in coords[i+1:]:
        (x2, y2, z2) = e2
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
        sqr_dist = dx * dx + dy * dy + dz * dz
        sqr_dists.append((e1, e2, sqr_dist))
sqr_dists.sort(key=lambda x: x[2])

coord_to_circuit = { }
circuit_to_coords = defaultdict(list)
circuit_ix = 0

connected = set()
connections = 0

for (coord1, coord2, _) in sqr_dists:
    # Part 1
    if connections == 1000:
        sizes = [len(coords) for coords in circuit_to_coords.values()]
        print(f"Part 1: {prod(sorted(sizes)[-3:])}")
    
    # Connect coords
    connected.update({ coord1, coord2 })
    connections += 1
    
    # Part 2
    if len(connected) == len(coords) and len(circuit_to_coords.keys()) == 1:
        print(f"Part 2: {coord1[0] * coord2[0]}")
        break
    
    circuit1 = coord_to_circuit.get(coord1, -1)
    circuit2 = coord_to_circuit.get(coord2, -1)

    # If neither are in a circuit, create a new circuit
    if circuit1 == -1 and circuit2 == -1:
        coord_to_circuit[coord1] = coord_to_circuit[coord2] = circuit_ix
        circuit_to_coords[circuit_ix].extend([coord1, coord2])
        circuit_ix += 1
    # If both are in the same circuit, skip
    elif circuit1 == circuit2: continue
    # If one is not in a circuit, add it to the other's circuit
    elif circuit1 == -1:
        coord_to_circuit[coord1] = circuit2
        circuit_to_coords[circuit2].append(coord1)
    elif circuit2 == -1:
        coord_to_circuit[coord2] = circuit1
        circuit_to_coords[circuit1].append(coord2)
    # Otherwise, merge the circuits
    else:
        circuit2_coords = circuit_to_coords.pop(circuit2)
        circuit_to_coords[circuit1].extend(circuit2_coords)
        for coord in circuit2_coords:
            coord_to_circuit[coord] = circuit1