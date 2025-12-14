#  Write a Python program to find the maximum and minimum value of the three given lists.
# Original lists: [2, 3, 5, 8, 7, 2, 3]
# [4, 3, 9, 0, 4, 3, 9]
# [2, 1, 5, 6, 5, 5, 4]
# Maximum value of the said three lists: 9
# Minimum value of the said three lists: 0

def find_the_minimum_val_three_lists(lst):
    return min(lst)

def find_the_maximum_val_three_lists(lst):
    return max(lst)

try:
    lst= []
    lst1= [int(val) for val in input('Please enter value of list1 separated with space: ').split()]
    print('='*60)

    lst2 = [int(val) for val in input('Please enter value of list2 separated with space: ').split()]
    print('=' * 60)

    lst3 = [int(val) for val in input('Please enter value of list3 separated with space: ').split()]
    print('=' * 60)

    lst+= lst1+lst2+lst3

except ValueError:
    print('Please enter integers only...')

except Exception:
    print('Something went wrong:( Try again...')

else:
    print(f'''Original lists: {lst1} \n {lst2} \n {lst3}
 Maximum value of the said three lists: {find_the_maximum_val_three_lists(lst)}
 Minimum value of the said three lists: {find_the_minimum_val_three_lists(lst)}''')