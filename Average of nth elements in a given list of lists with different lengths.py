#  Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
# Original list: [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths: [4.8, 5.8, 6.8, 8.0, 11.0]

def avg_inner_list(lst):
    olst= []
    max_len = 0
    for val in lst:
        if len(val) > max_len:
            max_len = len(val)

    for i in range(max_len):
        temp = []
        for val in lst:
            if i < len(val):
                temp.append(val[i])
        olst.append(sum(temp) / len(temp))
    return olst

try:
    lst= []
    n= int(input('Please enter how many inner list you want: '))
    print('='*60)
    if n <= 0:
        print('Please enter a positive integer')

    for i in range(n):
        ilst= [int(val) for val in input('Please enter your list elements separated with space: ').split()]
        lst.append(ilst)

except ValueError:
    print('Please enter a integer...')

except Exception:
    print('Something went wrong:( Please try again later...')

else:
    print(f'''Original list: {lst}
 Average of n-th elements in the said list of lists with different lengths: {avg_inner_list(lst)}''')