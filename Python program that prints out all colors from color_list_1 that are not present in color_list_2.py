# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data:
# color_list_1= set (["White", "Black", "Red"])
# color_list_2= set (["Red", "Green"])
# Expected Output:
# {'Black', 'White'}

def print_colors(lst1, lst2):
    color1_set= []
    for val in lst1:
        if val not in lst2:
            color1_set.append(val)
    return set(color1_set)

lst1= [val for val in input('Please enter your colors for list1 separated with space: ').split()]
print('='*60)

lst2= [val for val in input('Please enter your colors for list2 separated with space: ').split()]
print('='*60)

print(f'''color_list_1= {lst1}
color_list_@= {lst2}
{print_colors(lst1, lst2)}''')