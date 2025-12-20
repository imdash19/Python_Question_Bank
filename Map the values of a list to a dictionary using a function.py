# Write a Python program to map the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
# Sample Output: {1: 1, 2: 4, 3: 9}

def map_values_to_dict(lst):
    dictionary = {}
    for val in lst:
        dictionary[val] = val ** 2
    return dictionary

try:
    lst= [int(val) for val in input('Please enter your values separated with space: ').split()]

except ValueError:
    print('Please enter integers only...')

except:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original list: {lst}
Output: {map_values_to_dict(lst)}''')