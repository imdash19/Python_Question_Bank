# Write a Python program to find the first repeated character in a given string.

s = input()

seen = set()

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)
else:
    print("No repeated character")