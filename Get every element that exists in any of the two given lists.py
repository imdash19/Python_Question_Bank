# Write a Python program to get every element that exists in any of the two given lists once, after applying the provided function to each element of both.
# Sample Output: [2.2, 4.1]

def func(x):
    return round(x, 1)

list1 = [1, 2]
list2 = [3, 4]

result = list(set(map(func, list1 + list2)))
print(result)