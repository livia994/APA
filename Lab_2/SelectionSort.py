import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def time_selection_sort(arr):
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    return end_time - start_time

def analyze_sorting_algorithm(algorithm, input_sizes):
    times = []
    for size in input_sizes:
        arr = generate_random_array(size)
        execution_time = algorithm(arr)
        print(f"Input Size: {size}, Execution Time: {execution_time:.6f} seconds")
        times.append(execution_time)
    return times

def plot_results(input_sizes, times):
    plt.plot(input_sizes, times)
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Selection Sort Analysis')
    plt.show()

if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 5000, 10000]
    selection_sort_times = analyze_sorting_algorithm(time_selection_sort, input_sizes)
    plot_results(input_sizes, selection_sort_times)
