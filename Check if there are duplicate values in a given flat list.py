# 	Write a Python program to check if there are duplicate values in a given flat list.
# Original list: [1, 2, 3, 4, 5, 6, 7]
# Check if there are duplicate values in the said given flat list: False
# Original list: [1, 2, 3, 3, 4, 5, 5, 6, 7]
# Check if there are duplicate values in the said given flat list: True

def has_duplicates(lst):
    return len(lst) != len(set(lst))

lst = [int(val) if val.lstrip('-').isdigit() else val for val in input('Please enter your values separated with space: ').split()]

print('=' * 60)
print(f'''Original list: {lst}
Check if there are duplicate values in the said given flat list: {has_duplicates(lst)}''')