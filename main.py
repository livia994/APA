import time
import matplotlib.pyplot as plt

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Define the series of Fibonacci terms to be looked up
series1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
series2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Measure the execution time for each value in series1
execution_times_series1 = []
for n in series1:
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    execution_times_series1.append(end_time - start_time)

# Plotting the results for series1
plt.plot(series1, execution_times_series1, marker='o', linestyle='-')
plt.xlabel('Fibonacci Term')
plt.ylabel('Time (seconds)')
plt.title('Execution Time of Recursive Fibonacci Algorithm (Series 1)')
plt.grid(True)
plt.show()

# Print execution times for each Fibonacci term in series1
print("Series 1 (Limited Scope)")
print("Fibonacci Term\tExecution Time (seconds)")
for n, time_taken in zip(series1, execution_times_series1):
    print(f"{n}\t\t{time_taken:.6f} seconds")
