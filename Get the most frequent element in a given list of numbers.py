# 	Write a Python program to get the most frequent element in a given list of numbers.
# Original list: [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list: 2
# Original list: [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
# Item with maximum frequency of the said list: 3

def count_most_frequent_element(lst):
    ulst= []
    cnt= 0
    max_val= 0
    for val in lst:
        if val not in ulst:
            ulst.append(val)
    for val in ulst:
        if cnt < lst.count(val):
            cnt= lst.count(val)
            max_val= val
    return max_val

lst= [int(val) for val in input('Please enter your values separated with space: ').split()]
print('='*60)
print(f'''Original list: {lst}
Item with maximum frequency of the said list: {count_most_frequent_element(lst)}''')