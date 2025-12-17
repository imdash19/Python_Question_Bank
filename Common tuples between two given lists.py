# Write a Python program to find the common tuples between two given lists.
# Original lists: [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# [('red', 'green'), ('orange', 'pink')]
# Common tuples between two said lists [('orange', 'pink'), ('red', 'green')]
# Original lists: [('red', 'green'), ('orange', 'pink')]
# [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# Common tuples between two said lists [('orange', 'pink'), ('red', 'green')]

def common_tuples_between_two_list(lst1, lst2):
    olst= []
    for val in lst1:
        if val in lst2:
            olst.append(val)
    return olst

try:
    lst1= []
    lst2= []

    m= int(input('Please enter how many tuples you want in list1: '))

    for i in range(m):
        print('='*60)
        print(f'Inside {i+1} inner tuple')
        print('='*60)
        itup= [val for val in input('Please enter your tuple values separated with space: ').split()]
        lst1.append(tuple(itup))

    n= int(input('Please enter how many tuples you want in list2: '))

    for i in range(n):
        print('='*60)
        print(f'Inside {i+1} inner tuple')
        print('='*60)
        itup= [val for val in input('Please enter your tuple values separated with space: ').split()]
        lst2.append(tuple(itup))


except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original lists: {lst1} \n {lst2}
 Common tuples between two said lists: {common_tuples_between_two_list(lst1, lst2)}''')