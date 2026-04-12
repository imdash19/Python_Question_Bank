# Write a Python program to find a valid substring of a given string that contains matching brackets, at least one of which is nested.
# Input: ]][][[]]]
# Output: [[]]
# Input: ]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[[
# Output: [[][][][]]

s = input().strip()

stack = []
start = -1
max_len = 0
result = ""
depth = 0
nested = False

for i in range(len(s)):
    if s[i] == '[':
        stack.append(i)
        depth += 1
        if depth > 1:
            nested = True
    else:
        if stack:
            stack.pop()
            depth -= 1
            if stack:
                length = i - stack[-1]
                substr = s[stack[-1]+1:i+1]
            else:
                length = i - start
                substr = s[start+1:i+1]
            if length > max_len and nested:
                max_len = length
                result = substr
        else:
            start = i
            depth = 0
            nested = False

print(result)