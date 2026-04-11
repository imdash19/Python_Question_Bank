# Write a Python program to find the index of the matching parentheses for each character in a given string.
# Input: ()(())
# Output: [1, 0, 5, 4, 3, 2]
# Input: ()()()
# Output: [1, 0, 3, 2, 5, 4]
# Input: ((()))
# Output: [5, 4, 3, 2, 1, 0]

s = input().strip()

stack = []
res = [0] * len(s)

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        j = stack.pop()
        res[i] = j
        res[j] = i

print(res)