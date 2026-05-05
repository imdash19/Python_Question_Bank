# Write a Python program that takes a string and returns # on both sides of each element, which are not vowels.
# Sample Data:
# ("Green" -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"

s = input()
vowels = "aeiouAEIOU"

result = ""

for ch in s:
    if ch in vowels:
        result += ch
    else:
        result += "-" + ch + "-"

print(result)