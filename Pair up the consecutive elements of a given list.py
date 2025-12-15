#  Write a Python program to pair up the consecutive elements of a given list.
# Original lists: [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list: [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# Original lists: [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list: [[1, 2], [2, 3], [3, 4], [4, 5]]

def pairup_list(lst):
    olst= []
    for i in range(len(lst)-1):
        olst.append(lst[i:i+2])
    return olst

try:
    lst= [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your list values separated with space: ').split()]
    print('='*60)

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original lists: {lst}
 Pair up the consecutive elements of the said list: {pairup_list(lst)}''')