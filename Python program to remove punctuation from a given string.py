# Write a Python program to remove punctuation from a given string.
# Sample Output:
# Original text:
# String! With. Punctuation?
# After removing Punctuations from the said string:
# String With Punctuation

import string

text = input("Enter a string:\n")

result = ""
for ch in text:
    if ch not in string.punctuation:
        result += ch

print("After removing Punctuations from the said string:")
print(result)