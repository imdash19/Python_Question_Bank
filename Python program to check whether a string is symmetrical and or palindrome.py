# Write a Python program to check whether a string is symmetrical and/or palindrome. 
# The program should accept a string input. A string is symmetrical if both halves are equal. 
# A string is palindrome if it reads same backward. 
# The program should test both conditions independently.
# The output should clearly state the result.

s= input()

if s == s[::-1]:
    print('Symmetrical and Palindrome')

elif s[:len(s)//2] == s[len(s)//2:]:
    print('Symmetrical only')

else:
    print('Neither')
