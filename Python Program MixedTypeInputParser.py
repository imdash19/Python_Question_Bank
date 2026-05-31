# Reads input containing a mix of integers and strings in a single line, preserving each element's appropriate type. The program intelligently determines whether each token should be an integer or string.

tokens = input().split()

result = []

for item in tokens:
    if item.lstrip('-').isdigit():
        result.append(int(item))
    else:
        result.append(item)

print(result)
