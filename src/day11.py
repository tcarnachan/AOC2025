import networkx as nx
from collections import defaultdict

with open('res/day11.txt') as f:
    content = f.read()
    nodes = set(content.replace(':', "").split())
    lines = content.splitlines()

# Part 1
G = nx.DiGraph()
G.add_nodes_from(nodes)
for line in lines:
    split = line.split(': ')
    edge_start = split[0]
    for edge_end in split[1].split():
        G.add_edge(edge_start, edge_end)

print("Part 1:", len(list(nx.all_simple_paths(G, 'you', 'out'))))

# Part 2
goes_to = defaultdict(list)
comes_from = defaultdict(list)
for line in lines:
    split = line.split(': ')
    edge_start = split[0]
    for edge_end in split[1].split():
        goes_to[edge_start].append(edge_end)
        comes_from[edge_end].append(edge_start)

def get_paths_excl(exclude):
    server, out = 'svr', 'out'
    
    # no edges go to 'svr'
    cache = {}
    for node in goes_to[server]:
        cache[(server, node)] = 1

    def num_paths(start, end):
        if (start, end) in cache:
            return cache[(start, end)]
        res = 0
        for node in comes_from[end]:
            if node not in exclude:
                res += num_paths(start, node)
        cache[(start, end)] = res
        return res
    
    return num_paths(server, out)

all = get_paths_excl([])
excl_both = get_paths_excl(['dac', 'fft'])
excl_dac = get_paths_excl(['dac'])
excl_fft = get_paths_excl(['fft'])
print("Part 2:", all - excl_dac - excl_fft + excl_both)