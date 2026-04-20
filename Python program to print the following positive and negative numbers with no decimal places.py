# Write a Python program to print the following positive and negative numbers with no decimal places.

nums = input("Enter numbers separated by space: ").split()

for n in nums:
    print("{:+.0f}".format(float(n)))