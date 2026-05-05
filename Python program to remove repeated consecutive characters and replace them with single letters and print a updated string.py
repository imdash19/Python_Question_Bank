# Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"

s = input()

result = s[0]

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        result += s[i]

print(result)