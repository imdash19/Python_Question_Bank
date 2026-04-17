# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# Sample Words: red, white, black, red, green, black
# Expected Result: black, green, red, white, red

s = input()

words = s.split(',')

cleaned = [w.strip() for w in words]

unique_words = sorted(set(cleaned))

print(', '.join(unique_words))