# Write a Python program to find the indices of all occurrences of a given item in a given list.
# Sample Input:
# ([1,2,3,4,5,2], 2)
# ([3,1,2,3,4,5,6,3,3], 3)
# ([1,2,3,-4,5,2,-4], -4)
# Sample Output:
# Original list of numbers: [1, 2, 3, 4, 5, 2]
# Given Number 2
# Indices of all occurrences of the said item in the given list:
# [1, 5]
# Original list of numbers: [3, 1, 2, 3, 4, 5, 6, 3, 3]
# Given Number 3
# Indices of all occurrences of the said item in the given list:
# [0, 3, 7, 8]
# Original list of numbers: [1, 2, 3, -4, 5, 2, -4]
# Given Number -4
# Indices of all occurrences of the said item in the given list:
# [3, 6]
# Original list of numbers: [1, 2, 3, 4, 5, 2]
# Given Number 7
# Indices of all occurrences of the said item in the given list:
# []

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
x=int(input())
res=[]
for i in range(len(l)):
    if l[i]==x:
        res.append(i)
print("Original list of numbers:",l)
print("Given Number",x)
print("Indices of all occurrences of the said item in the given list:")
print(res)