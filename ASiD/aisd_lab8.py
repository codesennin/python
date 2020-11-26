import matplotlib.pyplot as plt
import networkx as nx
from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from ASiD import linked_list_fifo_queue as fifo


class GraphVisualization:
    # source https://www.geeksforgeeks.org/visualize-graphs-in-python/
    visual: List[List[int]]

    def __init__(self):
        self.visual = []

    def addEdge(self, a: int, b: int):
        self.visual.append([a, b])

    def visualize(self):
        graph = nx.Graph()
        graph.add_edges_from(self.visual)
        nx.draw_networkx(graph)
        plt.show()

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int):
        self.data = data
        self.index = index

    def __repr__(self):
        return f"{self.data}"


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.destination}"


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any):
        index = len(self.adjacencies)
        self.adjacencies[Vertex(data, index)] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == 1:  # directed
            self.add_directed_edge(source, destination, weight)
        else:  # undirected
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        keys = self.getVertexs()
        visited = []
        que = fifo.Queue()
        que.enqueue(keys[0])
        while len(que) != 0:
            v = que.dequeue()
            visit(v)
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited:
                    que.enqueue(neighbour.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        keys = self.getVertexs()
        visited = []
        v = keys[0]
        self._traverse_depth_first(v, visited, visit)

    def _traverse_depth_first(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visit(v)
        visited.append(v)
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self._traverse_depth_first(neighbour.destination, visited, visit)

    def show(self):
        graph = GraphVisualization()
        for key in self.adjacencies.keys():
            for edge in self.adjacencies[key]:
                graph.addEdge(edge.source, edge.destination)
        graph.visualize()

    def print(self):
        for data in self.adjacencies:
            print(data, "---->", self.adjacencies[data], sep=" ")

    def getVertexs(self):
        keys = []
        for key in self.adjacencies.keys():
            keys.append(key)
        return keys


class GraphPath:
    graph: Graph

    def __init__(self, graph: Graph):
        self.graph = graph

    def _algDijkstry(self):
        pass

    def _in_bredth(self, destination: Vertex):
        keys = self.graph.getVertexs()
        visited = []
        que = fifo.Queue()
        que.enqueue(keys[0])
        while len(que) != 0:
            v = que.dequeue()
            visited.append(v)
            if destination in visited:
                break
            for neighbour in self.graph.adjacencies[v]:
                if neighbour.destination not in visited:
                    que.enqueue(neighbour.destination)

    def find_best_path(self):
        keys = self.graph.getVertexs()
        if self.graph.adjacencies[keys[0]][0].weight is None:
            self._in_bredth()
        else:
            self._algDijkstry()


def _visit(vertex: Vertex):
    print(vertex)


#################
#### EXAMPLE ####
#################

graph = Graph()
graph.create_vertex("A")
graph.create_vertex("B")
graph.create_vertex("C")
graph.create_vertex("D")

vertexs = graph.getVertexs()

graph.add(1, vertexs[0], vertexs[1])
graph.add(1, vertexs[0], vertexs[2])
graph.add(1, vertexs[1], vertexs[3])
graph.add(1, vertexs[2], vertexs[1])
graph.add(1, vertexs[2], vertexs[3])


# graph.print()
# graph.traverse_breadth_first(_visit)
# graph.traverse_depth_first(_visit)
# graph.show()