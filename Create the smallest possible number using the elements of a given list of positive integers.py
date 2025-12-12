#  Write a Python program to create the smallest possible number using the elements of a given list of positive integers.
# Original list: [3, 40, 41, 43, 74, 9]
# Smallest possible number using the elements of the said list of positive integers: 3404143749
# Original list: [10, 40, 20, 30, 50, 60]
# Smallest possible number using the elements of the said list of positive integers:
# 102030405060
# Original list: [8, 4, 2, 9, 5, 6, 1, 0]
# Smallest possible number using the elements of the said list of positive integers: 01245689

def create_smallest_number(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if str(lst[i]) + str(lst[j]) > str(lst[j]) + str(lst[i]):
                lst[i], lst[j] = lst[j], lst[i]

    val = ""
    for i in lst:
        val += str(i)

    return val

try:
    ilst = [int(val) for val in input('Please enter your values separated with space: ').split()]
    print('=' * 60)

    lst = []
    for val in ilst:
        if val >= 0:
            lst.append(val)

except ValueError:
    print('Please enter a number...')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: {lst}
Smallest possible number using the elements of the said list of positive integers: {create_smallest_number(lst)}''')