# Write a Python program to count the number of groups of non-zero numbers separated by zeros of a given list of numbers.
# Original list: [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
# Number of groups of non-zero numbers separated by zeros of the said list: 4

def count_groups_separated_by_zero(lst):
    cnt = 0
    in_group = False

    for val in lst:
        if val != 0 and not in_group:
            cnt += 1
            in_group = True
        elif val == 0:
            in_group = False

    return cnt

try:
    lst= [int(val) for val in input('Please enter your tuple values separated with space: ').split()]
    print('='*60)

except ValueError:
    print('Please enter integers only...')

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
 Number of groups of non-zero numbers separated by zeros of the said list: {count_groups_separated_by_zero(lst)}''')