# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
# Input: W3resource Python, Exercises.
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: The dance, held in the school gym, ended at midnight.
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
# Input: The colors in my studyroom are blue, green, and yellow.
# Output:
# [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

s = input()
s += ' '

wlst = []
slst = []

word = ''
sep = ''

for v in s:
    if v.isalpha() or v == '.':
        if sep:
            slst.append(sep)
            sep = ''
        word += v
    else:
        if word:
            wlst.append(word)
            word = ''
        sep += v

if sep:
    slst.append(sep)

print([wlst, slst])