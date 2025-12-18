# Write a Python program to group the elements of a list based on the given function and returns the count of elements in each group.
# Sample Output: {6: 2, 4: 1}
#     {3: 2, 5: 1}

def group_elements_and_count(lst, choice):
    olst = {}

    for val in lst:
        if choice == 1:  # double the number
            key = val * 2
        elif choice == 2:  # length of string
            key = len(val)

        if key in olst:
            olst[key] += 1
        else:
            olst[key] = 1

    return olst


try:
    print('Choose grouping function:')
    print('1 -> Double the number')
    print('2 -> Length of string')
    choice = int(input('Please enter your choice (1 or 2): '))

    if choice not in (1, 2):
        raise ValueError('Invalid choice')

    if choice == 1:
        lst = [int(val) for val in input('Please enter integer values separated with space: ').split()]
    else:
        lst = [val for val in input('Please enter string values separated with space: ').split()]

except ValueError:
    print('Please enter valid input...')

except:
    print('Something went wrong :( Please try again...')

else:
    print(f'Original list: {lst}')
    print(f'Grouped result with count: {group_elements_and_count(lst, choice)}')