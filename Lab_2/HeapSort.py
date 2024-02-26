import random
import time
import matplotlib.pyplot as plt

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def time_heap_sort(arr):
    start_time = time.time()
    heap_sort(arr)
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
    plt.title('Heap Sort Analysis')
    plt.show()

    for i, size in enumerate(input_sizes):
        print(f"Input Size: {size}, E_T: {times[i]:.6f} seconds")

if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 5000, 10000]
    heap_sort_times = analyze_sorting_algorithm(time_heap_sort, input_sizes)
    plot_results(input_sizes, heap_sort_times)
