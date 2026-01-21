# 	Write a Python program to check if all the elements of a list are included in another given list.
# Sample Output: True
#     False

def all_elements_included(lst1, lst2):
    return all(elem in lst2 for elem in lst1)

lst1 = [int(val) if val.lstrip('-').isdigit() else val
        for val in input('Please enter first list values separated by space: ').split()]
print('=' * 60)

lst2 = [int(val) if val.lstrip('-').isdigit() else val
        for val in input('Please enter second list values separated by space: ').split()]
print('=' * 60)

print(f"All elements of the first list are included in the second list! {all_elements_included(lst1, lst2)}")