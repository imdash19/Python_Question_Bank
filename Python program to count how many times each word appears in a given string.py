# Write a Python program to count how many times each word appears in a given string.
# The program should accept a sentence from the user
# Words are separated by spaces
# Convert all words to lowercase before counting
# Count the frequency of each word using basic logic
# Display the word and its frequency
# Print the result in alphabetical order of words

lst= input().split()
lst.sort()

d= {}
for val in lst:
    d[val]= lst.count(val)

for k, v in d.items():
    print(f'{k}:{v}')
