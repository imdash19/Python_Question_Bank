# Write a Python program that removes duplicate elements from a given array of numbers so that each element appears only once and returns the new length of the array.
# Sample Input:
# [0,0,1,1,2,2,3,3,4,4,4]
# [1, 2, 2, 3, 4, 4]
# Sample Output:
# 5
# 4

a = list(map(int, input().strip("[]").split(",")))

b = []
for i in a:
    if i not in b:
        b.append(i)

print(len(b))