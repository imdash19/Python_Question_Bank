#  Write a Python program to insert a specified element in a given list after every nth element.
# Original list: [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element: [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
# Original list: ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# Insert Z in said list after every 3 th element: ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']

def add_element_list(lst, n, idx):
    olst= []
    cnt= 0
    for i in lst[::idx]:
        olst.append(i)
        cnt+= 1

        if cnt == n:
            olst.append(i)
            cnt= 0
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ')]
    print('='*60)

    n= input('Please enter the number you want to add in list: ')
    print('='*60)
    n= int(n) if (n.lstrip('-')).isdigit() else n

    idx= int(input('Please enter after how many elements you want to add: '))
    print('='*60)

except ValueError:
    print('Please enter a number...')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
Insert {n} in said list after every {idx} elements: {add_element_list(lst, n, idx)}''')