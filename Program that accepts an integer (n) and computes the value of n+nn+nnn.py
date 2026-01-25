# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result: 615

def compute(n):
    return int(n) + int(n + n) + int(n + n + n)

n = input("Enter a number: ")
print('=' * 60)

if n.isdigit():
    print(compute(n))
else:
    print("Invalid input! Try again...")