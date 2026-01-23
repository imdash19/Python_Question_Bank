# 	Write a Python program to get every nth element in a given list.
# Sample Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     [2, 4, 6, 8, 10]
#     [5, 10]
#     [6]

def every_nth_element(lst, n):
    if n <= 0:
        return []
    return lst[n-1::n]


lst = [int(val) if val.lstrip('-').isdigit() else val
    for val in input('Please enter your values separated with space: ').split()]
print('=' * 60)

n = int(input('Please enter the value of n: '))
print('=' * 60)

print(f'''Original list elements: {lst}
Every {n}th element of the said list: {every_nth_element(lst, n)}''')