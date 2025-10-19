# Write a Python program to count integer in a given mixed list.
# Original list: [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list: 6

def count_integer():
    lst= [val for val in input("Please enter your values separated with space: ").split()]
    count= 0
    for val in lst:
        if val.isdigit() or val.lstrip('-').isdigit():
            count+= 1
    print("Original list: ", lst)
    print("Number of integers in the said mixed list: ", count)

count_integer()