# Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
# Input:
# ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
# Output:
# True
# Input:
# ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
# Output:
# True

lst= list(map(str, input('Enter your values separated with space: ').split()))
print('='*60)

print(lst[len(lst)-2] in lst[len(lst)-1])