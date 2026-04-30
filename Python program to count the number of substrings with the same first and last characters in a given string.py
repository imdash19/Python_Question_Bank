# Write a Python program to count the number of substrings with the same first and last characters in a given string.

def count_substrings(s):
    count = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1

    return count

s = input()
print(count_substrings(s))