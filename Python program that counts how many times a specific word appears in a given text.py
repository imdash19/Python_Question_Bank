# Write a program that counts how many times a specific word appears in a given text. The program takes a text string and a word as input, then uses regular expressions to find and count all occurrences of that word. The search is case-sensitive, meaning "Python" and "python" are treated as different words. The word must match as a complete word, not as part of another word.
# Input Format:

# First line: A text string (can contain letters, numbers, spaces, and punctuation)
# Second line: The word to search and count

# Output Format:

# Print "The word appears X times" where X is the count of occurrences

import re

text = input()
word = input()

count = len(re.findall(r'\b' + re.escape(word) + r'\b', text))

print(f"The word appears {count} times")
