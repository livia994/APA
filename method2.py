import time
import matplotlib.pyplot as plt


def fibonacci_matrix(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        F = [[1, 1], [1, 0]]
        power(F, n - 1)
        return F[0][0]


def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
    F[0][0], F[0][1], F[1][0], F[1][1] = x, y, z, w


def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)


# Series of numbers for Fibonacci terms
series_1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
series_2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Measure the time taken for each value of n in series 1
execution_times_series_1 = []
for n in series_1:
    start_time = time.time()
    _ = fibonacci_matrix(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_series_1.append(execution_time)
    print(f"For n = {n} (Series 1), execution time is {execution_time:.6f} seconds.")

# Measure the time taken for each value of n in series 2
execution_times_series_2 = []
for n in series_2:
    start_time = time.time()
    _ = fibonacci_matrix(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_series_2.append(execution_time)
    print(f"For n = {n} (Series 2), execution time is {execution_time:.6f} seconds.")

# Plotting the results for series 1
plt.plot(series_1, execution_times_series_1, marker='o', label='Series 1')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Matrix Power Fibonacci Algorithm (Series 1)')
plt.grid(True)
plt.legend()
plt.show()

# Plotting the results for series 2
plt.plot(series_2, execution_times_series_2, marker='o', label='Series 2')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Matrix Power Fibonacci Algorithm (Series 2)')
plt.grid(True)
plt.legend()
plt.show()
