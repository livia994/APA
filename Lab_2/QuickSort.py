import random
import time
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def time_quick_sort(arr):
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    return end_time - start_time

def analyze_sorting_algorithm(algorithm, input_sizes):
    times = []
    for size in input_sizes:
        arr = generate_random_array(size)
        execution_time = algorithm(arr)
        times.append(execution_time)
    return times

def plot_results(input_sizes, times):
    plt.plot(input_sizes, times)
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Quick Sort Analysis')
    plt.show()

    for i, size in enumerate(input_sizes):
        print(f"Input Size: {size}, Execution Time: {times[i]:.6f} seconds")

if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 5000, 10000]
    quick_sort_times = analyze_sorting_algorithm(time_quick_sort, input_sizes)
    plot_results(input_sizes, quick_sort_times)
