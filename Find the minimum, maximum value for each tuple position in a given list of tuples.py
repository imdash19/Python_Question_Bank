#  Write a Python program to find the minimum, maximum value for each tuple position in a given list of tuples.
# Original list: [(2, 3), (2, 4), (0, 6), (7, 1)]
# Maximum value for each tuple position in the said list of tuples: [7, 6]
# Minimum value for each tuple position in the said list of tuples: [0, 1]

try:
    n = int(input('Please enter how many tuples you would like to add to your list: '))
    print('-' * 60)

    lst = []
    max_t = []
    min_t = []

    for i in range(n):
        print(f'Inside {i + 1} tuple')
        print('=' * 60)
        ilst = []
        a = int(input('Please enter your first element: '))
        b = int(input('Please enter your second element: '))
        ilst.append(a)
        ilst.append(b)
        lst.append(ilst)

    ta = lst[0][0]
    tb = lst[0][1]

    for val in lst:
        a, b = val[0], val[1]
        if a > ta:
            ta = a
        if b > tb:
            tb = b
    max_t.append(ta)
    max_t.append(tb)

    ta = lst[0][0]
    tb = lst[0][1]

    for val in lst:
        a, b = val[0], val[1]
        if a < ta:
            ta = a
        if b < tb:
            tb = b
    min_t.append(ta)
    min_t.append(tb)

    olst = []
    for val in lst:
        olst.append(tuple(val))

except ValueError:
    print('Please enter only integers')

except Exception:
    print('Something went wrong! Please try again...')

else:
    print(f'''Original list: {olst}
Maximum value for each tuple position in the said list of tuples: {max_t}
Minimum value for each tuple position in the said list of tuples: {min_t}''')