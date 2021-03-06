import matplotlib.pyplot as plt
import networkx as nx
from enum import Enum
from typing import Any, Optional, Dict, List, Callable
# szczerze mówiąc nie pamiętam czy przypadkiem lekko nie edytowałem mojej fifo względem tego co wysyłałem jako
# pracę na pierwszą ocenę, w przypadku jakiegoś problemu proszę o kontakt to wyślę atualny plik
from ASiD import linked_list_fifo_queue as fifo


class GraphVisualization:
    # źródło inspiracji https://www.geeksforgeeks.org/visualize-graphs-in-python/
    # na potrzeby lab08 rozbudowałem klasę o ważone krawędzie (w poprzednim labie teoretycznie też wypadałoby, żeby tak było, ale dopiero tu faktycznie tego używamy)
    visual: List[List[int]]
    visualWeighted: List[List[int]]

    def __init__(self):
        self.visual = []
        self.visualWeighted = []

    def addEdge(self, a: int, b: int, weight: float = None):
        if weight is not None:
            self.visualWeighted.append([a, b, weight])
        else:
            self.visual.append([a, b])

    def visualize(self):
        graph = nx.DiGraph()
        if len(self.visualWeighted) != 0:
            graph.add_weighted_edges_from(self.visualWeighted)
        if len(self.visual) != 0:
                graph.add_edges_from(self.visual)
        nx.draw(graph, nx.planar_layout(graph), edge_color="black", width=2, with_labels=True, node_size=750, alpha=0.8, arrows=True)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, nx.planar_layout(graph), edge_labels=labels)
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
        elif edge == 2:  # undirected
            self.add_undirected_edge(source, destination, weight)
        else:
            raise Exception("Edge has only 2 types: 1 - directed, 2 - undirected")

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
                graph.addEdge(edge.source, edge.destination, edge.weight)
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

    def _algDijkstry(self, source: Vertex, destination: Vertex):
        costs, parents, keys = {}, {}, self.graph.getVertexs()
        for child_vertex in keys:
            costs[child_vertex], parents[child_vertex] = 2147483647, None
        for neighbour_vertex in self.graph.adjacencies[source]:
            costs[neighbour_vertex.destination], parents[neighbour_vertex.destination] = neighbour_vertex.weight, neighbour_vertex.source
        visited, path = [], []
        visited.append(source)
        vertex = min(costs, key=costs.get)
        while vertex is not None:
            visited.append(vertex)
            cost = costs[vertex]
            for edge in graph.adjacencies[vertex]:
                total_cost = cost + edge.weight
                if costs[edge.destination] > total_cost:
                    costs[edge.destination], parents[edge.destination] = total_cost, edge.source
            temp_costs = costs.copy()
            vertex = min(temp_costs, key=temp_costs.get)
            while vertex in visited:
                temp_costs.pop(vertex)
                if len(temp_costs.keys()) == 0:
                    vertex = None
                    break
                vertex = min(temp_costs, key=temp_costs.get)
        while destination is not None:
            path.append(destination)
            destination = parents[destination]
        path.reverse()
        print("Path:", path, sep=" ")
        self._showPath(path)

    def _in_bredth(self, source: Vertex, destination: Vertex):
        visited = []
        que = fifo.Queue()
        que.enqueue([source])
        while len(que) != 0:
            vertexs_queue = que.dequeue()
            last_vertex = vertexs_queue[-1]
            for neighbour in self.graph.adjacencies[last_vertex]:
                if neighbour.destination not in visited:
                    temp_path = vertexs_queue.copy()
                    temp_path.append(neighbour.destination)
                    que.enqueue(temp_path)
                    if neighbour.destination == destination:
                        path = temp_path
        print("Path:", path, sep=" ")
        self._showPath(path)

    def find_best_path(self, source: Vertex, destination: Vertex):
        keys = self.graph.getVertexs()
        if self.graph.adjacencies[keys[0]][0].weight is None:
            self._in_bredth(source, destination)
        else:
            self._algDijkstry(source, destination)

    def _showPath(self, path: List[Vertex]):
        graph = GraphVisualization()
        for x in range(len(path)-1):
            graph.addEdge(path[x], path[x+1])
        graph.visualize()


def _visit(vertex: Vertex):
    print(vertex)


#################
#### EXAMPLE ####
#################

graph = Graph()

graph.create_vertex(0)
graph.create_vertex(1)
graph.create_vertex(2)
graph.create_vertex(3)
graph.create_vertex(4)
graph.create_vertex(5)
graph.create_vertex(6)

vertexs = graph.getVertexs()

graph.add(1, vertexs[0], vertexs[2], 12)
graph.add(1, vertexs[0], vertexs[4], 7)
graph.add(1, vertexs[1], vertexs[4], 8)
graph.add(1, vertexs[2], vertexs[5], 14)
graph.add(1, vertexs[2], vertexs[6], 9)
graph.add(1, vertexs[3], vertexs[4], 13)
graph.add(1, vertexs[4], vertexs[5], 11)
graph.add(1, vertexs[4], vertexs[6], 11)
graph.add(1, vertexs[5], vertexs[6], 9)

graph.print()

graph.show()
path = GraphPath(graph)
path.find_best_path(vertexs[0], vertexs[5])


