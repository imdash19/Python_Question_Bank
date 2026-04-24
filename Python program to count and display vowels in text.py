# Write a Python program to count and display vowels in text.

s= input('Please enter your string: ')
c= 0
for v in s:
    if v in 'aeiou':
        c+= 1
        print(v)