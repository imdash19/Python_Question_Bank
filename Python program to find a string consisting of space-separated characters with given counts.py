# Write a Python program to find a string consisting of space-separated characters with given counts.
# Input: {'f': 1, 'o': 2}
# Output: f o o
# Input: {'a': 1, 'b': 1, 'c': 1}
# Output: a b c

d = eval(input())

res = []

for k in d:
    for i in range(d[k]):
        res.append(k)

print(' '.join(res))