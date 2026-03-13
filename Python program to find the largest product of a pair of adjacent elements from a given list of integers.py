# Write a Python program to find the largest product of a pair of adjacent elements from a given list of integers.
# Original list: [1, 2, 3, 4, 5, 6]
# Largest product of the pair of adjacent elements of the said list: 30
# Original list: [1, 2, 3, 4, 5]
# Largest product of the pair of adjacent elements of the said list: 20
# Original list: [2, 3]
# Largest product of the pair of adjacent elements of the said list: 6

lst=eval(input())
m=lst[0]*lst[1]
for i in range(len(lst)-1):
    p=lst[i]*lst[i+1]
    if p>m:
        m=p
print(m)