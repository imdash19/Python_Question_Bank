# Write a Python program to get the difference between two given lists,
# after applying the provided function to each list element of both.
# Sample Output: [1.2]
#                [{'x': 2}]

def get_difference_between_two_lists(lst1, lst2, func):
    olst1 = [func(val) for val in lst1]
    olst2 = [func(val) for val in lst2]

    diff = []
    for val in olst1:
        if val not in olst2:
            diff.append(val)

    for val in olst2:
        if val not in olst1:
            diff.append(val)

    return diff


try:
    lst1 = [float(val) for val in input('Please enter values for list1 separated with space: ').split()]
    print('=' * 60)
    lst2 = [float(val) for val in input('Please enter values for list2 separated with space: ').split()]
    print('=' * 60)

except ValueError:
    print('Please enter numeric values only...')

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Difference between the two lists:
{get_difference_between_two_lists(lst1, lst2, lambda x: round(x, 1))}''')