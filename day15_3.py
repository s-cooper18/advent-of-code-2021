import numpy as np
from functools import reduce
import networkx as nx
from collections import deque

data = []

def increment_base_ten(this_int):
    new_int = (this_int + 1) if this_int < 9 else 1
    return str(new_int)

def increment_x_times(this_int, x):
    for i in range(x):
        this_int = increment_base_ten(int(this_int))
    return str(this_int)

with open("input.txt", "r") as f:
    for row in f.read().split("\n"):
        this_row = []
        new_row = row
        this_row.append(new_row)
        for i in range(4):
            new_row = "".join([increment_base_ten(int(elem)) for elem in new_row])
            this_row.append(new_row)
        data.append("".join(this_row))
        #data = [row for row in f.read().split("\n")]

old_data = data.copy()
# append down
for i in range(1,5):
    for row in old_data:
        new_row = "".join([increment_x_times(int(elem), i) for elem in row])
        data.append(new_row)


# create the full map



n_rows = len(data)
n_cols = len(data[0])

n_diagonals = n_rows + n_cols - 1

coords = [(row, col) for count in range(n_diagonals) for row in range(n_rows) for col in range(n_cols) if row + col == count]
node_weights = [int(data[row][col]) for count in range(n_diagonals) for row in range(n_rows) for col in range(n_cols) if row + col == count]

weights = {}
for i in range(len(coords)):
    weights[coords[i]] = node_weights[i]

weights[(0,0)] = 0
shortest_dist = {}
shortest_dist[(0,0)] = 0


def get_surrounding_coords(row, col):
    diag_num = row + col
    possible_coords = []
    if col != 0:
        possible_coords.append((row, col - 1))
    if row != 0:
        possible_coords.append((row - 1, col))
    if col + 1 != n_cols:
        possible_coords.append((row, col + 1))
    if row + 1 != n_rows:
        possible_coords.append((row + 1, col))
    return possible_coords

# create a graph
def init_graph(coords):
    graph = nx.Graph()
    for coord in coords:
        for coord2 in get_surrounding_coords(coord[0], coord[1]):
            graph.add_edge(coord, coord2, weight = weights[coord2])
    return graph

graph = init_graph(coords)

start_node = (0,0)

end_node = (len(data) - 1, len(data[0]) - 1)

path = nx.dijkstra_path(graph, start_node, end_node)
initial_guess = sum(list(map(lambda x: weights[x], path)))

def calc_dijikstra_dist(graph, next_node, end_node):
    _, path = nx.algorithms.shortest_paths.weighted.bidirectional_dijkstra(graph, next_node, end_node, weight='weight')
    return sum(list(map(lambda x: weights[x], path)))


def visit_node(this_node, best_dist):
    if this_node == end_node:
        return best_dist

    for next_node in (node for node in graph.neighbors(this_node) if node != (0,0)):
        if shortest_dist.get(next_node) == None:
            shortest_dist[next_node] = shortest_dist[this_node] + weights[next_node]
        else:
            neighbors = (node for node in graph.neighbors(next_node) if shortest_dist.get(node) != None)
            new_dist = min([shortest_dist[n] for n in neighbors])
            shortest_dist[next_node] = new_dist + weights[next_node]

    return best_dist
        

# depth first search to see if this is actually the best path
this_node = start_node

nodes = nx.dfs_preorder_nodes(graph, (0,0))

print(list(nodes))

n_attempts = 10

for i in range(n_attempts):
    for node in nx.dfs_preorder_nodes(graph, (0,0)):
        best_dist = visit_node(node, initial_guess)
    print(shortest_dist[end_node])

#for node in graph.nodes():
#    best_dist = visit_node(this_node, initial_guess)


#m = visit_node(start_node, initial_guess)
#print(m)

print(end_node)
    
