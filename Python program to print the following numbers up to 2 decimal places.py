# Write a Python program to print the following numbers up to 2 decimal places.

nums = input("Enter numbers separated by space: ").split()

for n in nums:
    print("{:.2f}".format(float(n)))