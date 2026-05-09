# You need to write a program that checks whether a given string begins with a specific character that the user provides.Think of it like this: Imagine you have a sentence and you want to know if it starts with a particular letter. For example, does the sentence "Hello World" start with the letter "H"? The answer would be yes. But does it start with "h" (lowercase)? The answer would be no, because we treat uppercase and lowercase letters as different characters.Here's how your program will work: First, you will ask the user to enter any text or sentence. Then, you will ask them to enter a single character that they want to check. Your program will then examine whether the text starts with that exact character and give them an answer.You will use Python's re module (Regular Expressions) for this task. Specifically, you'll use a special symbol called the caret ^ which is used in regex to indicate the beginning of a string. This is the proper way to check the starting character without using simple string methods like slicing.Input Format:

# First line: Enter any string (text, sentence, or words)
# Second line: Enter a single character to check
# Output Format:

# Print "String starts with the character" if the string begins with the given character
# Print "String does not start with the character" if the string does not begin with the given character

import re

text = input()
char = input()

pattern = "^" + re.escape(char)

if re.search(pattern, text):
    print("String starts with the character")
else:
    print("String does not start with the character")
