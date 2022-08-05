"""
Exemple de design pattern Adapter.
"""
from heapq import heappush, heappop


class Node:
    """Représente un noeud d'un graph"""

    def __init__(self, name, edges=[]):
        self.edges = edges
        self.name = name

    def __repr__(self):
        return self.name


class Edge:
    """Représente une arête d'un graph entre deux noeuds"""

    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

    def __lt__(self, other):
        return False

    def __repr__(self):
        return f"{self.from_node} -> {self.to_node}"


class NodeAdapter:
    def __init__(self, node):
        self.node = node

    @property
    def name(self):
        return self.node.name

    @property
    def out_edges(self):
        return [EdgeAdapter(edge) for edge in self.node.edges]

    def __repr__(self):
        return self.node.name

    def __lt__(self, other):
        return False

    def __str__(self):
        return super.__str__(self)


class EdgeAdapter:
    def __init__(self, edge):
        self.edge = edge

    @property
    def tail(self):
        return NodeAdapter(self.edge.from_node)

    @property
    def head(self):
        return NodeAdapter(self.edge.to_node)

    def __repr__(self):
        return f"{self.tail} -> {self.head}"


def short_path(start_node, end_node, weight_func=lambda edge: 1):
    """Calcule le plus court chemin entre deux noeuds d'un graph
    Une Node représete un point contenant une liste d'arêtes sortantes (out_edges)
    Un Edge représete une arête entre deux noeuds (head et tail qui sont des Nodes)
    Arguments:
        start_node: Node
        end_node: Node
        weight_func: fonction qui calcule le poids d'une arête
    retourne:
        une liste de noeuds qui représente le plus court chemin entre les deux noeuds
    """
    shortest_paths = {start_node.name: (0, None)}

    edge_heap = []  # Ma heap de edges
    for edge in start_node.out_edges:  # Pour chaque edge de start_node
        heappush(edge_heap, (weight_func(edge), edge))  # Ajoute l'edge dans la heap avec son poids
    print(edge_heap)
    while edge_heap:  # Tant que la heap n'est pas vide
        path_weight, edge = heappop(edge_heap)  # On prend le poids du plus petit edge et on le retire de la heap
        if (edge.head not in shortest_paths) or (shortest_paths[edge.head.name][0] > path_weight):
            shortest_paths[edge.head.name] = (path_weight, edge)
            for out_edge in edge.head.out_edges:
                heappush(edge_heap, (path_weight + weight_func(out_edge), out_edge))
    print([type(key) for key in shortest_paths.keys()], type(end_node), end_node.name in shortest_paths)
    if end_node.name not in shortest_paths:
        err = ("No connection from node %s" % str(start_node) + " to node %s." % str(end_node))
        raise Exception(err)
    path_weight = shortest_paths[end_node][0]
    path_edges = [shortest_paths[end_node][1]]
    current_node = path_edges[-1].tail
    while current_node is not start_node:
        path_edges.append(shortest_paths[current_node][1])
        current_node = path_edges[-1].tail
    # list[start:end:step]
    return path_edges[::-1], path_weight


A = Node("A")
B = Node("B")
C = Node("C")

AB = Edge(A, B)
BC = Edge(B, C)

A.edges = [AB]
B.edges = [BC]
adapter_A = NodeAdapter(A)
adapter_B = NodeAdapter(B)
print(A.edges)
print(short_path(adapter_A, adapter_B))