# Write a Python program to compute the cumulative sum of numbers in a given list.
# Note: Cumulative sum = sum of itself + all previous numbers in the said list.
# Sample Input:
# [10, 20, 30, 40, 50, 60, 7]
# [1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5]
# Sample Output:
# [10, 30, 60, 100, 150, 210, 217]
# [1, 3, 6, 10, 15]
# [0, 1, 3, 6, 10, 15]

lst=eval(input())
s=0
res=[]
for i in lst:
    s+=i
    res.append(s)
print(res)