#  Write a Python program to create a new list dividing two given lists of numbers.
# Original list: [7, 2, 3, 4, 9, 2, 3]
#           [7, 2, 3, 4, 9, 2, 3]
#           [0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]

def divide_two_list(lst1, lst2):
    olst= []
    for a,b in zip(lst1, lst2):
        if b == 0:
            olst.append("Infinity")
        else:
            olst.append(a / b)
    return olst

try:
    lst1= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated by space: ').split()]
    print('='*60)

    lst2= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated by space: ').split()]
    print('='*60)

except ValueError:
    print('Please enter numbers only...')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: {lst1}
{lst2}
{divide_two_list(lst1, lst2)}''')