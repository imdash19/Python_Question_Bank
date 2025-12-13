#  Write a Python program to convert a given list of tuples to a list of strings.
# Original list of tuples: [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# Convert the said list of tuples to a list of strings: ['red green', 'black white', 'orange pink']
# Original list of tuples: [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
# Convert the said list of tuples to a list of strings: ['Laiba Delacruz', 'Mali Stacey Drummond', 'Raja Welch', 'Saarah Stone']

def convert_list_of_tuples_to_list_of_strings(lst):
    olst= []
    for val in lst:
        value= ''
        for vl in val:
            value+= str(vl) + ' '
        olst.append(value.strip())
    return olst

try:
    lst= []
    n= int(input('Please enter how many inner tuple you want: '))
    print('='*60)
    for i in range(n):
        print(f'Inside {i+1} inner tuple')
        print('='*60)
        ilst= [val for val in input('Please enter your values separated with space: ').split()]
        lst.append(tuple(ilst))
        print('='*60)

except ValueError:
    print('Please enter a whole number...')

except Exception:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original list of tuples: {lst}
 Convert the said list of tuples to a list of strings: {convert_list_of_tuples_to_list_of_strings(lst)}''')