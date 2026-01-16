# 	Write a Python program to find the items that are parity outliers in a given list.
# Sample Output: [1, 3]
#     [2, 4, 6]

lst = list(map(int, input("Enter list elements: ").split()))

evens = [x for x in lst if x % 2 == 0]
odds = [x for x in lst if x % 2 != 0]

outliers = odds if len(evens) > len(odds) else evens
print(outliers)