#  Write a Python program to find the indexes of all None items in a given list.
# Original list: [1, None, 5, 4, None, 0, None, None]
# Indexes of all None items of the list: [1, 4, 6, 7]

def indexes_of_None_items_in_given_list(lst):
    olst= []
    for i in range(len(lst)):
        if lst[i] is None:
            olst.append(lst.index(val))
    return olst

try:
    lst= []
    n= int(input('Please enter how many inputs you want: '))

    for i in range(n):
        print('='*60)
        print(f'Inside {i+1} inner list')
        print('=' * 60)
        val= input('Please enter your input: ')
        if (val.lstrip('-')).isdigit():
            lst.append(int(val))
        elif (val.lstrip('-')).isdecimal():
            lst.append(float(val))
        elif len(val) == 0:
            lst.append(None)
        else:
            lst.append(val)

except:
    print('Something went wrong :( Try again later...')

else:
    print(f'''Original list: {lst}
 Indexes of all None items of the list: {indexes_of_None_items_in_given_list(lst)}''')