# Write a Python program to calculate the time runs (difference between start and current time) of a program.

import time
def main():
    start_time = time.time()
    print("Program started...")
    for i in range(int(input("Enter a number to simulate work: "))):
        pass
    end_time = time.time()
    runtime = end_time - start_time

    print("\nProgram finished.")
    print(f"Execution Time: {runtime:.6f} seconds")
main()