# Write a PYTHON program to scramble the letters of string in a given list.
# 	Original list:
# 	['PYTHON', 'list', 'exercises', 'practice', 'solution']
# 	After scrambling the letters of the strings of the said list:
# 	['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

import random

words = ['PYTHON', 'list', 'exercises', 'practice', 'solution']
scrambled_words = []

for w in words:
    scrambled = ''.join(random.sample(w, len(w)))
    scrambled_words.append(scrambled)

print("Original list:")
print(words)
print("\nAfter scrambling the letters of the strings of the said list:")
print(scrambled_words)