#  Write a Python program to traverse a given list in reverse order, also print the elements with original index.
# Original list: ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order: black
#     white
#     green
#     red
# Traverse the said list in reverse order with original index: 3 black
#  2 white
#  1 green
#  0 red

def traverse_given_lsit(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i])

    for i in range(len(lst) - 1, -1, -1):
        print(i, lst[i])

try:
    lst= [val for val in input('Please enter your values separated with space: ').split()]

except Exception:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
 Traverse the said list in reverse order: {traverse_given_lsit(lst)}''')