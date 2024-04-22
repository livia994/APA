import networkx as nx
import matplotlib.pyplot as plt
import time
import sys

class GraphAnalyzer:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def dfs(self, start):
        visited = set()
        traversal = []
        self.dfs_util(start, visited, traversal)
        return traversal

    def dfs_util(self, v, visited, traversal):
        visited.add(v)
        traversal.append(v)
        for neighbour in self.graph.neighbors(v):
            if neighbour not in visited:
                self.dfs_util(neighbour, visited, traversal)

    def generate_random_graph(self, num_vertices, edge_probability):
        self.graph = nx.fast_gnp_random_graph(num_vertices, edge_probability, directed=False)

    def analyze(self):
        sizes = [10, 50, 100]  # Graph sizes
        densities = [0.1, 0.5, 0.9]  # Edge densities

        time_data = {'Size 10': [], 'Size 50': [], 'Size 100': []}
        memory_data = {'Size 10': [], 'Size 50': [], 'Size 100': []}

        for size in sizes:
            for density in densities:
                self.generate_random_graph(size, density)

                # Measure time
                start_time = time.time()
                self.dfs(0)
                end_time = time.time()
                execution_time = end_time - start_time
                time_data[f'Size {size}'].append(execution_time)

                # Measure memory usage
                memory_usage = sys.getsizeof(self.graph)
                memory_data[f'Size {size}'].append(memory_usage)

                print(f"Graph Size: {size}, Density: {density}")
                print(f"Execution Time: {execution_time} seconds")
                print(f"Memory Usage: {memory_usage} bytes")
                print("---------------------------------------")

        # Plotting execution time
        plt.figure(figsize=(10, 5))
        for size, times in time_data.items():
            plt.plot(densities, times, marker='o', label=size)
        plt.xlabel('Edge Density')
        plt.ylabel('Execution Time (seconds)')
        plt.title('DFS Execution Time for Different Graph Sizes')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plotting memory usage
        plt.figure(figsize=(10, 5))
        for size, memories in memory_data.items():
            plt.plot(densities, memories, marker='o', label=size)
        plt.xlabel('Edge Density')
        plt.ylabel('Memory Usage (bytes)')
        plt.title('DFS Memory Usage for Different Graph Sizes')
        plt.legend()
        plt.grid(True)
        plt.show()

analyzer = GraphAnalyzer()
analyzer.analyze()
