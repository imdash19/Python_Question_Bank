# Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits. Return True if the employee code is valid and False if it's not.
# Sample Input:
# ('12345678')
# ('1234567j')
# ('12345678j')
# ('123456789123')
# ('123456abcdef')
# Sample Output:
# True
# False
# False
# True
# False

s=input("Enter employee code: ")

print(True) if s.isdigit() and (len(s)==8 or len(s)==12) else print(False)