# Write a Python function to insert a string in the middle of a string.
# Sample function and result:
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def insert_string_middle(s, word):
    mid = len(s) // 2
    return s[:mid] + word + s[mid:]

s = input()
word = input()

print(insert_string_middle(s, word))