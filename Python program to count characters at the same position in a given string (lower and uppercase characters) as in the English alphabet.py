# Write a Python program to count characters at the same position in a given string (lower and uppercase characters) as in the English alphabet.

s = input().strip()
count = 0

for i in range(len(s)):
    if ord(s[i].lower()) - ord('a') == i:
        count += 1

print(count)