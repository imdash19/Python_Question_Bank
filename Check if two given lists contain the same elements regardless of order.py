# 	Write a Python program to check if two given lists contain the same elements regardless of order.
# Original list elements: [1, 2, 4]
#   [2, 4, 1]
# Check two said lists contain the same elements regardless of order! True
# Original list elements: [1, 2, 3]
#   [1, 2, 3]
# Check two said lists contain the same elements regardless of order! True
# Original list elements: [1, 2, 3]
#   [1, 2, 4]
# Check two said lists contain the same elements regardless of order! False

def check_same_elements(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

lst1= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
print('='*60)

lst2= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
print('='*60)

print(f"""Original list: {lst1}
{lst2}
Check two said lists contain the same elements regardless of order! {check_same_elements(lst1, lst2)}""")