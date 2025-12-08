#  Write a Python program to concatenate element-wise three given lists.
# Original lists: ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists: ['0red100', '1green200', '2black300', '3blue400', '4white500']

try:
    lst= []
    i= int(input("Please enter how many list you want to enter: "))
    print('='*60)
    for ir in range(i):
        slst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Enter values separated with space: ').split()]
        print('='*60)
        lst.append(slst)
    olst= []
    for group in zip(*lst):
        combined = ""
        for item in group:
            combined = combined + str(item)
        olst.append(combined)

except ValueError:
    print('Please enter a number...')

except Exception as e:
    print(e)

else:
    print('Original lists: ')
    for val in lst:
        print(val)
    print(f'Concatenate element-wise three said lists: {olst}')