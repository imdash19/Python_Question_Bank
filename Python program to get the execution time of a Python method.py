# Write a Python program to get the execution time of a Python method.

import time

def sample_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

start_time = time.perf_counter()
sample_function()
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")