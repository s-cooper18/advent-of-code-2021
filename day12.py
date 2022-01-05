import networkx as nx


from functools import reduce

with open("input.txt", "r") as f:
    data = f.read()

lines = data.split("\n")


graph = nx.Graph()

for line in lines:
    nodes = line.split('-')
    graph.add_edge(nodes[0], nodes[1])

finished_paths = []

def depth_first_search(this_node, path, visited_twice_small_cave):
    path.append(this_node)
    if this_node == 'end':
        finished_paths.append(path)
        print(path)
        return
    else:
        neighbours = [node for node in graph.neighbors(this_node) if node != 'start']
        for node in neighbours:
            if node.islower() and node in path:
                # lower coords

                if visited_twice_small_cave != '':
                    continue
                else:
                    depth_first_search(node, path.copy(), node)
            else:
                new_path = path.copy()
                depth_first_search(node, new_path, visited_twice_small_cave)


depth_first_search("start", [], '')
print(len(finished_paths))

