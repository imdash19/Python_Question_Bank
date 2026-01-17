# 	Write a Python program to create a dictionary with the unique values of a given list as keys and their frequencies as the values.
# Sample Output: {'a': 4, 'b': 2, 'f': 2, 'c': 1, 'e': 2}
#     {3: 4, 4: 2, 7: 1, 5: 2, 9: 1, 0: 1, 2: 1}

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(input("Enter element: "))
freq_dict = {}

for item in lst:
    freq_dict[item] = freq_dict.get(item, 0) + 1

print(freq_dict)