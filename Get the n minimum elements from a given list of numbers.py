# 	Write a Python program to get the n minimum elements from a given list of numbers.
# Sample Output:
# Original list elements: [1, 2, 3]
# Minimum values of the said list: [1]
# Original list elements: [1, 2, 3]
# Two minimum values of the said list: [1, 2]
# Original list elements: [-2, -3, -1, -2, -4, 0, -5]
# Three minimum values of the said list: [-5, -4, -3]
# Original list elements: [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
# Two minimum values of the said list: [2, 2.2]

n = int(input("Enter number of elements in the list: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter element {i + 1}: "))
    numbers.append(num)

k = int(input("Enter how many minimum elements you want: "))
print("Original list elements:", numbers)
result = sorted(numbers)[:k]
print(f"{k} minimum values of the said list:", result)