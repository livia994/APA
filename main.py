import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

series_1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
series_2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

execution_times_series_1 = []
for n in series_1:
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_series_1.append(execution_time)

execution_times_series_2 = []
for n in series_2:
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_series_2.append(execution_time)

# Plotting the results for series 1
plt.plot(series_1, execution_times_series_1, marker='o', label='Series 1')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Recursive Fibonacci Algorithm (Series 1)')
plt.grid(True)
plt.legend()
plt.show()

# Plotting the results for series 2
plt.plot(series_2, execution_times_series_2, marker='o', label='Series 2')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Recursive Fibonacci Algorithm (Series 2)')
plt.grid(True)
plt.legend()
plt.show()
