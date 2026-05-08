# Write a Python program to check whether a string contains all vowels (a, e, i, o, u).
# The program should accept a string input from the user.
# Case should be ignored. The program must check each vowel.
# The output should display TRUE if all vowels exist, else FALSE.

s= input()
temp= []

for v in s:
    if v in 'aeiou' and v not in temp:
        temp.append(v)

temp.sort()
if temp == ['a', 'e', 'i', 'o', 'u']:
    print(True)
else:
    print(False)
