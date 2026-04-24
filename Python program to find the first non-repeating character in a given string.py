# Write a Python program to find the first non-repeating character in a given string.

s = input("Enter a string: ")
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
else:
    print("No non-repeating character found")