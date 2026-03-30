# Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True otherwise False.
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# [False, False, False, False]
# Input:
# ['ca t', 'car', 'fea r', 'cente r']
# Output:
# [True, False, True, True]

lst= [val for val in input('Please enter your value separated with comma: ').split(',')]
olst= []
for val in lst:
    if val.__contains__(' '):
        olst.append(True)
    else:
        olst.append(False)
print(olst)