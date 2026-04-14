# Given a string consisting of groups of matched nested parentheses separated by parentheses, write a Python program to compute the depth of each group.
# Input: (()) (()) () ((()()()))
# Output: [2, 2, 1, 3]
# Input: () (()) () () () ()
# Output: [1, 2, 1, 1, 1, 1]
# Input: (((((((()))))))) () (()) ((()()()))
# Output: [8, 1, 2, 3]

s = input().strip().split()

res = []

for group in s:
    depth = 0
    max_depth = 0
    for ch in group:
        if ch == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        else:
            depth -= 1
    res.append(max_depth)

print(res)