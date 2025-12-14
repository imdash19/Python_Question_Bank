#  Write a Python program to remove all strings from a given list of tuples.
# Original list: [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# Remove all strings from the said list of tuples: [(100,), (80,), (90,), (88, 89), (90, 92)]

def remove_string_from_list_of_tuples(lst):
    olst= []
    for val in lst:
        ilst= []
        for value in val:
            if type(value) != str:
                ilst.append(value)
        olst.append(tuple(ilst))
    return olst

try:
    lst= []
    n= int(input('Please enter how many inner tuples you want: '))
    if n< 0:
        raise ValueError('Please enter a positive integer')

    for i in range(n):
        print('='*60)
        print(F'Inside {i+1} inner tuple')
        print('=' * 60)
        ilst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your tuple values separated with space: ').split()]
        print('='*60)
        lst.append(tuple(ilst))

except ValueError:
    print('Please enter an integer...')

except Exception:
    print("Oops! Something went wrong:( Try again...")

else:
    print(f'''Original list: {lst}
 Remove all strings from the said list of tuples: {remove_string_from_list_of_tuples(lst)}''')