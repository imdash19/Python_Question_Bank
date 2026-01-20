# 	Write a Python program to get the powerset of a given iterable.
# Sample Output:
# Original list elements: [1, 2]
# Powerset of the said list: [(), (1,), (2,), (1, 2)]
# Original list elements: [1, 2, 3, 4]
# Powerset of the said list: [(), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)]

from itertools import combinations
data = eval(input("Enter a list: "))
print("Original list elements:", data)
powerset = []
for r in range(len(data) + 1):
    powerset.extend(combinations(data, r))

print("Powerset of the said list:", powerset)