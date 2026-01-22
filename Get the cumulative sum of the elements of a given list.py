# 	Write a Python program to get the cumulative sum of the elements of a given list.
# Original list elements: [1, 2, 3, 4]
# Cumulative sum of the elements of the said list: [1, 3, 6, 10]
# Original list elements: [-1, -2, -3, 4]
# Cumulative sum of the elements of the said list: [-1, -3, -6, -2]

def get_cumulative_sum(lst):
    slst = [lst[0]]
    for i in range(1, len(lst)):
        slst.append(slst[-1] + lst[i])
    return slst

lst = [int(val) for val in input('Please enter your values separated with space: ').split()]
print('=' * 60)

print(f'''Original list elements: {lst}
Cumulative sum of the elements of the said list: {get_cumulative_sum(lst)}''')