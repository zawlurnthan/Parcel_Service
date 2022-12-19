# Zaw Than, Student ID:#001368744

import csv


class Graph:
    """

        Create graph and its methods.
        Graph is a datastructure which acts as a map to keep all places and its distances in it.

    """

    def __init__(self):
        self.places = {}
        self.distances = {}

    def add_vertex(self, v):
        self.places[v] = []

    def add_directed_edge(self, u, v, weight):
        self.distances[(u, v)] = weight
        self.places[u].append(v)

    def add_undirected_edge(self, a, b, weight):
        self.add_directed_edge(a, b, weight)
        self.add_directed_edge(b, a, weight)

    def search(self, u, v):
        return self.distances[(u, v)]

    def get_key(self, value):
        """ Get the key by value. O(N) """
        for k, v in self.distances.items():
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
    graph = Graph()

    next(reader)
    fields = next(reader)

    for row in reader:
        address = row[1]
        graph.add_vertex(address)

        for i in range(2, len(row)):
            distance = row[i]
            if distance:
                graph.add_undirected_edge(fields[i], address, float(row[i]))
    return graph
