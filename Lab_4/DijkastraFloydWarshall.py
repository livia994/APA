import heapq
import sys
import time
import random
import matplotlib.pyplot as plt

def dijkstra(graph, source):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[source] = 0
    visited = [False] * num_nodes

    pq = [(0, source)]
    shortest_paths = {source: [source]}

    while pq:
        dist, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True

        for neighbor, weight in enumerate(graph[node]):
            if weight > 0:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
                    shortest_paths[neighbor] = shortest_paths[node] + [neighbor]  # Update shortest path

    return distances, shortest_paths


def floyd_warshall(graph):
    num_nodes = len(graph)
    distances = [[float('inf')] * num_nodes for _ in range(num_nodes)]

    # Initialize distances matrix with direct edges weights
    for i in range(num_nodes):
        for j in range(num_nodes):
            distances[i][j] = graph[i][j]

    # Update distances using dynamic programming
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

def generate_random_sparse_graph(num_nodes, density=0.2):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < density:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

def generate_random_dense_graph(num_nodes, edge_density=0.5):
    graph = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_density:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight
            else:
                graph[i][j] = float('inf')
                graph[j][i] = float('inf')
                # Alternatively, you can leave the default value as 0
    return graph


# Analyze the performance and output shortest paths for different graph sizes
graph_sizes = [50, 100, 150, 200, 250, 300]
runtimes_dijkstra_sparse = []
runtimes_dijkstra_dense = []
runtimes_floyd_warshall_sparse = []
runtimes_floyd_warshall_dense = []

for size in graph_sizes:
    print(f"\nPerforming analysis for graphs with {size} nodes:")
    time.sleep(1)  # Delay for 1 second

    # Generate a random sparse graph
    print("Using Dijkstra's algorithm for sparse graph...")
    time.sleep(1)  # Delay for 1 second
    graph_sparse = generate_random_sparse_graph(size)
    source_node_sparse = random.randint(0, size - 1)

    # Run Dijkstra's algorithm for sparse graph
    start_time = time.time()
    distances_sparse, shortest_paths_sparse = dijkstra(graph_sparse, source_node_sparse)
    end_time = time.time()
    runtime_dijkstra_sparse = end_time - start_time
    runtimes_dijkstra_sparse.append(runtime_dijkstra_sparse)

    # Print shortest paths for sparse graph
    print(f"\nShortest paths found by Dijkstra's algorithm for a sparse graph with {size} nodes (source: {source_node_sparse}):")
    time.sleep(1)  # Delay for 1 second
    for node in range(size):
        if node != source_node_sparse:
            print(f"Node {node}: Distance = {distances_sparse[node]}, Path = {shortest_paths_sparse[node]}")
    time.sleep(1)  # Delay for 1 second

    print("Using Floyd-Warshall algorithm for sparse graph...")
    time.sleep(1)  # Delay for 1 second
    # Run Floyd-Warshall algorithm for sparse graph
    start_time = time.time()
    distances_floyd_sparse = floyd_warshall(graph_sparse)
    end_time = time.time()
    runtime_floyd_warshall_sparse = end_time - start_time
    runtimes_floyd_warshall_sparse.append(runtime_floyd_warshall_sparse)

    # Print shortest paths for sparse graph
    print(f"\nShortest paths found by Floyd-Warshall algorithm for a sparse graph with {size} nodes:")
    time.sleep(1)  # Delay for 1 second
    for i in range(size):
        for j in range(size):
            if i != j:
                print(f"Node {i} to Node {j}: Distance = {distances_floyd_sparse[i][j]}")
    time.sleep(1)  # Delay for 1 second

    # Generate a random dense graph
    print("Using Dijkstra's algorithm for dense graph...")
    time.sleep(1)  # Delay for 1 second
    graph_dense = generate_random_dense_graph(size)
    source_node_dense = random.randint(0, size - 1)

    # Run Dijkstra's algorithm for dense graph
    start_time = time.time()
    distances_dense, shortest_paths_dense = dijkstra(graph_dense, source_node_dense)
    end_time = time.time()
    runtime_dijkstra_dense = end_time - start_time
    runtimes_dijkstra_dense.append(runtime_dijkstra_dense)

    # Print shortest paths for dense graph
    print(f"\nShortest paths found by Dijkstra's algorithm for a dense graph with {size} nodes (source: {source_node_dense}):")
    time.sleep(1)  # Delay for 1 second
    for node in range(size):
        if node != source_node_dense:
            print(f"Node {node}: Distance = {distances_dense[node]}, Path = {shortest_paths_dense[node]}")
    time.sleep(1)  # Delay for 1 second

    print("Using Floyd-Warshall algorithm for dense graph...")
    time.sleep(1)  # Delay for 1 second
    # Run Floyd-Warshall algorithm for dense graph
    start_time = time.time()
    distances_floyd_dense = floyd_warshall(graph_dense)
    end_time = time.time()
    runtime_floyd_warshall_dense = end_time - start_time
    runtimes_floyd_warshall_dense.append(runtime_floyd_warshall_dense)

    # Print shortest paths for dense graph
    print(f"\nShortest paths found by Floyd-Warshall algorithm for a dense graph with {size} nodes:")
    time.sleep(1)  # Delay for 1 second
    for i in range(size):
        for j in range(size):
            if i != j:
                print(f"Node {i} to Node {j}: Distance = {distances_floyd_dense[i][j]}")
    time.sleep(1)  # Delay for 1 second

# Plot the results
plt.plot(graph_sizes, runtimes_dijkstra_sparse, marker='o', label='Dijkstra (Sparse)')
plt.plot(graph_sizes, runtimes_dijkstra_dense, marker='o', label='Dijkstra (Dense)')
plt.plot(graph_sizes, runtimes_floyd_warshall_sparse, marker='o', label='Floyd-Warshall (Sparse)')
plt.plot(graph_sizes, runtimes_floyd_warshall_dense, marker='o', label='Floyd-Warshall (Dense)')
plt.title("Performance Comparison of Dijkstra's and Floyd-Warshall Algorithms")
plt.xlabel("Number of Nodes")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.show()
