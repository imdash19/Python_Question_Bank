# Write a Python program to find a substring in a given string that contains a vowel between two consonants.
# Input: Hello
# Output: Hel
# Input: Sandwhich
# Output: San
# Input: Python
# Output: hon

s = input()
vowels = 'aeiouAEIOU'

for i in range(len(s) - 2):
    sub = s[i:i+3]
    if sub[0] not in vowels and sub[1] in vowels and sub[2] not in vowels:
        print(sub)
        break