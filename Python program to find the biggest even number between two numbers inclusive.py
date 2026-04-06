# Write a Python program to find the biggest even number between two numbers inclusive.
# Input: m = 12, n = 51
# Output: 50
# Input: m = 1, n = 79
# Output:78
# Input: m = 47, n = 53
# Output: 52
# Input: m = 100, n = 200
# Output: 200

m,n= map(int, input().split())
if max(m, n) % 2 == 0:
    print(max(m, n))
else:
    print(max(m, n)-1)