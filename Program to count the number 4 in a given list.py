# Write a Python program to count the number 4 in a given list.

def count_four(lst):
    count = 0
    for val in lst:
        if val == 4:
            count += 1
    return count

lst= [int(val) for val in input('Please enter your list of numbers separated with space: ').split()]
print(count_four(lst))