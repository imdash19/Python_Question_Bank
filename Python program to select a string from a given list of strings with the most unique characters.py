# Write a Python program to select a string from a given list of strings with the most unique characters.
# Input:
# [cat, catatatatctsa, abcdefhijklmnop, 124259239185125, '', foo, unique]
# Output:
# abcdefhijklmnop
# Input:
# [Green, Red, Orange, Yellow, '', White]
# Output:
# Orange

lst= [val for val in input().split(', ')]
olst= [set(val) for val in lst]
temp= 0
idx= 0

for val in olst:
    if len(val) > temp:
        idx= olst.index(val)
        temp= len(val)

print(lst[idx])