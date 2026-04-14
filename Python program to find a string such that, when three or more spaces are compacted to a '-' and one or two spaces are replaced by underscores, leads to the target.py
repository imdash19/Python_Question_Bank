# Write a Python program to find a string such that, when three or more spaces are compacted to a '-' and one or two spaces are replaced by underscores, leads to the target.
# Input: Python-Exercises
# Output: Python Exercises
# Input: Python_Exercises
# Output: Python Exercises
# Input: -Hello,_world!__This_is-so-easy!-
# Output: Hello, world! This is so easy!

s = input()

s = s.replace('-', '   ')
s = s.replace('_', ' ')

words = s.split()
result = ' '.join(words)

print(result)