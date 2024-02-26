import random
import time
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


def time_merge_sort(arr):
    start_time = time.time()
    merge_sort(arr)
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
    plt.title('Merge Sort Analysis')
    plt.show()


if __name__ == "__main__":
    input_sizes = [100, 500, 1000, 5000, 10000]
    merge_sort_times = analyze_sorting_algorithm(time_merge_sort, input_sizes)
    plot_results(input_sizes, merge_sort_times)
    print("Input Size\tExecution Time (seconds)")
    print("--------------------------------------")
    for i in range(len(input_sizes)):
        print(f"{input_sizes[i]}\t\t{merge_sort_times[i]}")
