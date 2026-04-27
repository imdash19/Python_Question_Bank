# Write a Python program to find the maximum length of consecutive 0's in a given binary string.

s = input().strip()

max_len = 0
current = 0

for ch in s:
    if ch == '0':
        current += 1
        if current > max_len:
            max_len = current
    else:
        current = 0

print(max_len)