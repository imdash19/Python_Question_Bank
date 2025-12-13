#  Write a Python program to sort a given list of tuples on specified element.
# Original list of tuples: [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# Sort on 1st element of the tuple of the said list: [('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
# Sort on 2nd element of the tuple of the said list: [('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
# Sort on 3rd element of the tuple of the said list: [('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]

def sort_list_of_tuples_on_specified_element(lst, ie):
    return sorted(lst, key=lambda x: x[ie - 1])

try:
    lst = []
    ll = int(input('Enter how many inner tuple you want: '))
    print('-' * 60)

    for i in range(ll):
        print('=' * 60)
        print(f'Inside {i+1} inner tuple')
        ilst = [val if not val.lstrip('-').replace('.', '', 1).isdigit()
                else float(val) if '.' in val else int(val)
                for val in input(
                    'Please enter tuple values separated with space: ').split()]
        lst.append(tuple(ilst))

    print('=' * 60)
    ie = int(input('Please enter the element index to sort by: '))
    print('=' * 60)

except ValueError:
    print('Please enter a number...')

except Exception:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original list of tuples: {lst}
Sort on {ie} element of the tuple of the said list:
{sort_list_of_tuples_on_specified_element(lst, ie)}''')