# # Write a Python program to display the first and last colors from the following list.
# color_list= ["Red", "Green", "White", "Black"]

def get_first_last_color(lst):
    return lst[0], lst[-1]

lst= [val for val in input('Please enter your colors separated with space: ').split()]
print('='*60)

if len(lst) >= 2:
    get_first_last_color(lst)

else:
    print("Please enter atleast 2 colors")