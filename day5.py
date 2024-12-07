from collections import defaultdict
import sys

import networkx as nx
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)


def visualize_directed_graph(edges):
    """
    Visualize a directed graph.

    Parameters:
        edges (list of tuples): List of edges where each edge is represented as (source, target).
    """
    # Create a directed graph
    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    # Draw the graph
    pos = nx.spring_layout(graph)  # Layout for better visualization
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=3000,
        arrowsize=20,
    )
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels={(u, v): "" for u, v in graph.edges()}
    )

    plt.title("Directed Graph")
    plt.show()


with open("./sample/day5.txt", "r") as f:
    result = 0

    takingPaths = True
    path = []
    update = []
    for line in f:
        line = line.strip()
        if not line:
            takingPaths = False
            continue

        if takingPaths:
            a, b = list(map(int, line.split("|")))
            path.append((a, b))
        else:
            a = list(map(int, line.split(",")))
            update.append(a)
    visualize_directed_graph(path)
    tree = defaultdict(list)
    for a, b in path:
        tree[a].append(b)

    def look(val, s, visited, up):
        print(val, s, visited, "BROOO")
        if val in s:
            print(s, val, "FALSED")
            return False
        if val not in tree:
            return True
        visited.add(val)
        # print("-", val, up)
        for i in tree[val]:
            if i in visited:
                continue
            if not look(i, s, visited, up):
                print(up, val, s)
                return False
        return True

    for up in update:
        s = set()
        valid = True

        for u in up:
            visited = set()
            print(
                "=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            )
            if not look(u, s, visited, up):
                valid = False
                break
            s.add(u)
        if valid:
            print(up, "hole")
            result += up[len(up) // 2]
    print(result)
