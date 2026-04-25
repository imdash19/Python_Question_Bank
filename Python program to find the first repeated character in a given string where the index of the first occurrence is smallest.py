# Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.

s = input()

for i in range(len(s)):
    if s[i] in s[i+1:]:
        print(s[i])
        break
else:
    print("No repeated character")