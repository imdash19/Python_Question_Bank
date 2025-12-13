#  Write a Python program to calculate the maximum and minimum sum of a sub list in a given list of lists.
# Original list: [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Maximum sum of sub list of the said list of lists: [2, 3, 5, 4]
# Minimum sum of sub list of the said list of lists: [1, 2, 1, 2]

def cal_sum(lst):
    olst= []
    for val in lst:
        olst.append(sum(val))
    return olst

def max_sublist(lst):
    olst= cal_sum(lst)
    max_idx= olst.index(max(olst))
    return lst[max_idx]

def min_sublist(lst):
    olst= cal_sum(lst)
    min_idx= olst.index(min(olst))
    return lst[min_idx]

try:
    lst= []
    n= int(input("Enter how many inner list you want: "))
    for i in range(n):
        print(f'Inside {i+1} inner list')
        print('='*60)
        ilst= [int(val) for val in input('Please enter your values separated with space: ').split()]
        lst.append(ilst)
        print('='*60)

except ValueError:print('Please enter only integers separated with space')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: {lst}
 Maximum sum of sub list of the said list of lists: {max_sublist(lst)}
 Minimum sum of sub list of the said list of lists: {min_sublist(lst)}''')