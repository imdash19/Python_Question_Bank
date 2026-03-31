# Write a Python program to find a list of strings that have fewer total characters (including repetitions).
# Input:
# [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
# Output:
# ['this', 'list', 'is', 'narrow']
# Input:
# [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
# Output:
# ['Red', 'Black', 'Pink']

n = int(input())
lst = []

for i in range(n):
    ilst = input().split()
    lst.append(ilst)

min_len = float('inf')
result = []

for sub in lst:
    total = sum(len(word) for word in sub)
    if total < min_len:
        min_len = total
        result = sub

print(result)