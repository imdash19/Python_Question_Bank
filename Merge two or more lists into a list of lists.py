# Write a Python program to merge two or more lists into a list of lists, combining elements from each of the input lists based on their positions.
# Sample Output:
# After merging lists into a list of lists: [['a', 1, True], ['b', 2, False]]
#   [['a', 1, True], [None, 2, False]]
#   [['a', 1, True], ['_', 2, False]]

def merge_two_or_more_lists_into_a_list_of_lists(lst, fill_value=None):
    olst = []

    max_len = max(len(inner) for inner in lst)

    for i in range(max_len):
        temp = []
        for inner in lst:
            if i < len(inner):
                temp.append(inner[i])
            else:
                temp.append(fill_value)
        olst.append(temp)

    return olst


try:
    n = int(input('Please enter how many lists you want to enter: '))
    if n < 2:
        raise ValueError('Please enter two or more lists to continue...')

    lst = []
    for i in range(n):
        ilst = [
            int(val) if val.lstrip('-').isdigit()
            else True if val == 'True'
            else False if val == 'False'
            else val
            for val in input(f'Please enter values for list {i + 1}: ').split()
        ]
        lst.append(ilst)

except ValueError:
    print('Please enter a valid number...')

except:
    print('Something went wrong :( Please try again...')

else:
    print('\nOriginal lists:')
    for val in lst:
        print(val)

    print('\nAfter merging lists into a list of lists:')
    print(merge_two_or_more_lists_into_a_list_of_lists(lst))

    print('\nUsing None as fill value:')
    print(merge_two_or_more_lists_into_a_list_of_lists(lst, None))

    print('\nUsing "_" as fill value:')
    print(merge_two_or_more_lists_into_a_list_of_lists(lst, '_'))