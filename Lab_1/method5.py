import time
import matplotlib.pyplot as plt

def fibonacci_binomial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

# Series of numbers for Fibonacci terms
series_1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
series_2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Measure the execution time for each value of n in series 1
execution_times_series_1 = []
for n in series_1:
    start_time = time.time()
    fibonacci_binomial(n)
    end_time = time.time()
    execution_times_series_1.append(end_time - start_time)
    print(f"For n = {n} (Series 1), execution time is {execution_times_series_1[-1]:.6f} seconds.")

# Measure the execution time for each value of n in series 2
execution_times_series_2 = []
for n in series_2:
    start_time = time.time()
    fibonacci_binomial(n)
    end_time = time.time()
    execution_times_series_2.append(end_time - start_time)
    print(f"For n = {n} (Series 2), execution time is {execution_times_series_2[-1]:.6f} seconds.")

# Plotting the results for series 1
plt.plot(series_1, execution_times_series_1, marker='o', linestyle='-', label='Series 1')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Binomial Coefficients Fibonacci Algorithm (Series 1)')
plt.grid(True)
plt.legend()
plt.show()

# Plotting the results for series 2
plt.plot(series_2, execution_times_series_2, marker='o', linestyle='-', label='Series 2')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Binomial Coefficients Fibonacci Algorithm (Series 2)')
plt.grid(True)
plt.legend()
plt.show()
