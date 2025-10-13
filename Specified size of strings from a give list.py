# Write a Python program to extract specified size of strings from a give list of string values.
# 	Original list: ['Python', 'list', 'exercises', 'practice', 'solution']
# 	length of the string to extract: 8
# 	After extracting strings of specified length from the said list: ['practice', 'solution']

def get_specified_size_string(n):
    lst= [val for val in input("Please enter your strings with space: ").split()]
    print("-"*60)
    olst= []
    for val in lst:
        if len(val) >= n:
            olst.append(val)
    print(olst)

get_specified_size_string(int(input("Please enter your length: ")))