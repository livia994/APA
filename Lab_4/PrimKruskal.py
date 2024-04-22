import heapq
import random
import timeit
import matplotlib.pyplot as plt

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.rank[u] = 0
        elif u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                root_u, root_v = root_v, root_u
            self.parent[root_v] = root_u
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1

# Prim's Algorithm
def prim(graph):
    MST = []
    visited = set()

    # Select arbitrary starting vertex
    start_vertex = next(iter(graph))
    heap = [(0, None, start_vertex)]  # (weight, parent, vertex)

    while heap:
        weight, parent, vertex = heapq.heappop(heap)
        if vertex not in visited:
            visited.add(vertex)
            if parent is not None:
                MST.append((parent, vertex, weight))
            for neighbor, w in graph[vertex]:
                heapq.heappush(heap, (w, vertex, neighbor))

    return MST


# Kruskal's Algorithm
def kruskal(graph):
    MST = []
    disjoint_set = DisjointSet()

    # Sort edges by weight
    edges = sorted([(u, v, w) for u in graph for v, w in graph[u]])

    for u, v, w in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            MST.append((u, v, w))

    return MST

# Generate random graph
def generate_random_graph(n):
    graph = {}
    for i in range(n):
        graph[i] = [(j, random.randint(1, 100)) for j in range(n) if j != i]
    return graph

# Measure execution time for Prim's algorithm
def measure_prim(graph):
    return timeit.timeit(lambda: prim(graph), number=1)

# Measure execution time for Kruskal's algorithm
def measure_kruskal(graph):
    return timeit.timeit(lambda: kruskal(graph), number=1)

# Experiment setup
sizes = [10, 20, 30, 40, 50]
results_prim = []
results_kruskal = []

# Run experiments and print results
print("Graph Size\tPrim's Time\tKruskal's Time")
print("--------------------------------------------")
for size in sizes:
    graph = generate_random_graph(size)
    time_prim = measure_prim(graph)
    time_kruskal = measure_kruskal(graph)
    results_prim.append(time_prim)
    results_kruskal.append(time_kruskal)
    print(f"{size}\t\t{time_prim:.6f}\t\t{time_kruskal:.6f}")

# Plotting
plt.plot(sizes, results_prim, label="Prim's Algorithm")
plt.plot(sizes, results_kruskal, label="Kruskal's Algorithm")
plt.xlabel('Graph Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of Prim\'s and Kruskal\'s Algorithms')
plt.legend()
plt.show()
