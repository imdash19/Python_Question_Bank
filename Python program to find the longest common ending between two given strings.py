# Write a Python program to find the longest common ending between two given strings.
# Original strings: running ruminating
# Common ending between said two strings: ing
# Original strings: thisisatest testing123testing
# Common ending between said two strings:

s1, s2 = input(), input()
temp = ''

for i in range(-1, -min(len(s1), len(s2)) - 1, -1):
    if s1[i] == s2[i]:
        temp += s1[i]
    else:
        break

print(temp[::-1])