# Write a Python program to randomize the order of the values of a list returning a new list.
# Sample Output: Original list: [1, 2, 3, 4, 5, 6]
# Shuffle the elements of the said list: [3, 2, 4, 1, 6, 5]
import random


def randomize_order_of_the_values(lst):
    olst= lst.copy()
    return random.shuffle(olst)

try:
    lst= [int(val) for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
Shuffle the elements of the said list: {randomize_order_of_the_values(lst)}''')