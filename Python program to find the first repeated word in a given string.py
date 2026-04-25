# Write a Python program to find the first repeated word in a given string.

text = input()

words = text.split()
seen = set()

for word in words:
    if word in seen:
        print(word)
        break
    seen.add(word)
else:
    print("No repeated word")