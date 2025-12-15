#  Write a Python program to move a specified element in a given list.
# Original list: ['red', 'green', 'white', 'black', 'orange']
# Move white at the end of the said list: ['red', 'green', 'black', 'orange', 'white']
# Original list: ['red', 'green', 'white', 'black', 'orange']
# Move red at the end of the said list: ['green', 'white', 'black', 'orange', 'red']
# Original list: ['red', 'green', 'white', 'black', 'orange']
# Move black at the end of the said list: ['red', 'green', 'white', 'orange', 'black']

def move_element(lst, ch):
    olst= lst.copy()
    olst.remove(ch)
    olst.append(ch)
    return olst

try:
    lst= [val for val in input('Please enter your list elements separated with space: ').split()]
    print('='*60)
    ch= input('Please enter your choice:')
    print('='*60)

except Exception:
    print('Something went wrong:( Please try again...')

else:
    print(f'''Original list: {lst}
 Move white at the end of the said list: {move_element(lst, ch)}''')