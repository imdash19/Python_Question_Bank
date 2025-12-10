#  Write a Python program to add a number to each element in a given list of numbers.
# Original lists: [3, 8, 9, 4, 5, 0, 5, 0, 3]
# Add 3 to each element in the said list: [6, 11, 12, 7, 8, 3, 8, 3, 6]
# Original lists: [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
# Add 0.51 to each element in the said list: [3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]

def add_element(lst, num):
    olst= []
    for val in lst:
        olst.append(val + num)
    return olst

try:
    lst= [float(val) for val in input('Please enter your values separated with space: ').split()]
    print('='*60)
    num= float(input('Please enter your number to add in each element: '))
    print('='*60)

except ValueError:
    print('Please enter only integers separated with space')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original lists: {lst}
Add {num} to each element in the said list: {add_element(lst, num)}''')