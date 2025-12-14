#  Write a Python program to find the dimension of a given matrix.
# Original list: [[1, 2], [2, 4]]
# Dimension of the said matrix: (2, 2)
# Original list: [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix: (2, 3)
# Original list: [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix: (3, 3)

try:
    lst= []
    n= int(input('Please enter how many inner list you want: '))

    if n <= 0:
        raise ValueError('Please enter a positive integer')

    m= int(input('Please enter how many inner list elements you want: '))

    if m <= 0:
        raise ValueError('Please enter a positive integer')

    for i in range(n):
        print('='*60)
        print(f'Inside {i+1} inner list')
        print('='*60)
        ilst= []
        for j in range(m):
            val= input('Please enter element of inner list element: ')
            ilst.append(int(val) if (val.lstrip('-')).isdigit() else val)
        lst.append(ilst)

except ValueError:
    print('Please enter a integer...')

except Exception:
    print('Something went wrong:( Plase try again later...')

else:
    print(f'''Original list: {lst}
 Dimension of the said matrix: ({n}, {m})''')