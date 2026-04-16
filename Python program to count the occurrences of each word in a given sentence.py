# Write a Python program to count the occurrences of each word in a given sentence.

s= input('Please enter a string: ')
d= {}

for c in s:
    d[c]= s.count(c)

print(d)