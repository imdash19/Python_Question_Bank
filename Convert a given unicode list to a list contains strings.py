#  Write a Python program to convert a given unicode list to a list contains strings.
# Original lists: ['S001', 'S002', 'S003', 'S004']
# Convert the said Unicode list to a list contains strings: ['S001', 'S002', 'S003', 'S004']

def convert_unicode_to_string(lst):
    olst= []
    for val in lst:
        olst.append(str(val))
    return olst

try:
    lst= [val for val in input('Please enter your unicode values separate dwith space: ').split()]

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original lists: {lst}
 Convert the said Unicode list to a list contains strings: {convert_unicode_to_string(lst)}''')