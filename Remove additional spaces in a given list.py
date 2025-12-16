# Write a Python program to remove additional spaces in a given list.
# Original list: ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
# Remove additional spaces from the said list: ['abc', '', '', 'sdfds', '', '', 'sdfds', 'huy']

def remove_spaces(lst):
    olst= []
    for val in lst:
        olst.append(val.strip())
    return olst

try:
    lst= []
    n= int(input('Please enter how many inputs you want: '))
    for i in range(n):
        print('='*60)
        val= input('Please enter your input: ')
        print('='*60)
        lst.append(val)

except ValueError:
    print('Please enter a number')

except:
    print('Something went wrong :( ')

else:
    print(f'''Original list: {lst}
 Remove additional spaces from the said list: {remove_spaces(lst)}''')