# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

lst= [val for val in input('Please enter your string: ').split()]
temp= lst[0]
for i in range(1, len(lst)):
    if len(temp) < len(lst[i]):
        temp= lst[i]

print(temp, len(temp))