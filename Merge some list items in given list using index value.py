#  Write a Python program to merge some list items in given list using index value.
# Original lists: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Merge items from 2 to 4 in the said List: ['a', 'b', 'cd', 'e', 'f', 'g']
# Merge items from 3 to 7 in the said List: ['a', 'b', 'c', 'defg']

def merge_elements(lst, a, b):
    olst= []
    for i in range(a):
        olst.append(lst[i])
    ch= ''
    for i in range(a, b+1):
        ch+= lst[i]
    olst.append(ch)
    for i in range(b+1, len(lst)):
        olst.append(lst[i])

    return olst

while True:
    try:
        lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
        print('='*60)

        a= int(input('Please enter your first index number: '))
        print('='*60)

        b= int(input('Please enter your second index number: '))
        print('='*60)

        print(f'''Original lists: {lst}
         Merge items from {a} to {b} in the said List: {merge_elements(lst, a, b)}''')
        print('='*60)

        print('''1. Do you want to continue
        2. Exit''')
        print('='*60)

        ch= int(input('Please enter your choice: '))
        print('='*60)

        match ch:
            case 1:
                print(f'''Merge items from {a} to {b} in the said List: {merge_elements(lst, a, b)}''')

            case 2:
                break

            case _:
                print('Invalid choice! Please try again...')

    except ValueError:
        print('Please enter an integer...')

    except Exception:
        print('Something went wrong! Please try again later...')