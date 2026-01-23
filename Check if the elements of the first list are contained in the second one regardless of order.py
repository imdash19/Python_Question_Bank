# 	Write a Python program to check if the elements of the first list are contained in the second one regardless of order.
# Sample Output: True
#     True
#     False
#     True

from collections import Counter

def is_contained(lst1, lst2):
    return not (Counter(lst1) - Counter(lst2))

lst1 = [int(val) if val.lstrip('-').isdigit() else val for val in input('Enter first list values separated by space: ').split()]

lst2 = [    int(val) if val.lstrip('-').isdigit() else val for val in input('Enter second list values separated by space: ').split()]

print('=' * 60)
print(is_contained(lst1, lst2))