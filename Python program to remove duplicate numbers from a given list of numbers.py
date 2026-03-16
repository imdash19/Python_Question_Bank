# Write a Python program to remove duplicate numbers from a given list of numbers.
# Sample Input:
# ([1,2,3,2,3,4,5])
# ([1,2,3,2,4,5])
# ([1,2,3,4,5])
# Sample Output:
# Original list of numbers: [1, 2, 3, 2, 3, 4, 5]
# After removing the duplicate numbers from the said list:
# [1, 4, 5]
# Original list of numbers: [1, 2, 3, 2, 4, 5]
# After removing the duplicate numbers from the said list:
# [1, 3, 4, 5]
# Original list of numbers: [1, 2, 3, 4, 5]
# After removing the duplicate numbers from the said list:
# [1, 2, 3, 4, 5]

n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
res=[]
for i in l:
    if l.count(i)==1:
        res.append(i)
print("Original list of numbers:",l)
print("After removing the duplicate numbers from the said list:")
print(res)