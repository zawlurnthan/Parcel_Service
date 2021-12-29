# Zaw Than, Student ID:#001368744

import csv


class Graph:
    """ Create graph and its methods. """

    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, v):
        self.adjacency_list[v] = []

    def add_directed_edge(self, u, v, weight):
        self.edge_weights[(u, v)] = weight
        self.adjacency_list[u].append(v)

    def add_undirected_edge(self, a, b, weight):
        self.add_directed_edge(a, b, weight)
        self.add_directed_edge(b, a, weight)

    def search(self, u, v):
        return self.edge_weights[(u, v)]

    def get_key(self, value):
        """ Get the key by value. O(N) """
        for k, v in self.edge_weights.items():
            if value == v:
                return k


""" 
    Pseudocode for get graph method 
        read csv file
        
        get address 
        get distance of two points
        add address and distance to graph
        return graph
"""


def get_graph():
    """ Create graph from distance csv file. O(N^2). """

    file = open('distance.csv')
    filtered = (line.replace('\n', '') for line in file)
    reader = csv.reader(filtered)
    g = Graph()

    next(reader)
    fields = next(reader)

    for row in reader:
        address = row[1]
        g.add_vertex(address)

        for i in range(2, len(row)):
            distance = row[i]
            if distance:
                g.add_undirected_edge(fields[i], address, float(row[i]))
    return g
