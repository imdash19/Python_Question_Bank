# 	Write a Python program to get the symmetric difference between two iterable, without filtering out duplicate values.
# Sample Output: [30, 40]

iterable1 = list(map(int, input("Enter first iterable elements: ").split()))
iterable2 = list(map(int, input("Enter second iterable elements: ").split()))

result = []

for item in iterable1:
    if item not in iterable2:
        result.append(item)

for item in iterable2:
    if item not in iterable1:
        result.append(item)

print("Symmetric Difference:", result)