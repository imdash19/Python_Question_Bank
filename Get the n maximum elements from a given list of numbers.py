# 	Write a Python program to get the n maximum elements from a given list of numbers.
# Sample Output:
# Original list elements: [1, 2, 3]
# Maximum values of the said list: [3]
# Original list elements: [1, 2, 3]
# Two maximum values of the said list: [3, 2]
# Original list elements: [-2, -3, -1, -2, -4, 0, -5]
# Three maximum values of the said list: [0, -1, -2]
# Original list elements: [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
# Two maximum values of the said list: [5.2, 4.6]

n = int(input("Enter number of elements in the list: "))

numbers = []
for i in range(n):
    num = float(input(f"Enter element {i + 1}: "))
    numbers.append(num)

k = int(input("Enter how many maximum elements you want: "))
print("Original list elements:", numbers)
result = sorted(numbers, reverse=True)[:k]
print(f"{k} maximum values of the said list:", result)