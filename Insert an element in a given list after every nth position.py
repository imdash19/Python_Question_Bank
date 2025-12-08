#  Write a Python program to insert an element in a given list after every nth position.
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# Insert 'a' in the said list after 2nd element: [1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
# Insert 'b' in the said list after 4 th element: [1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]

try:
    lst = [int(val) if val.lstrip('-').isdigit() else val for val in input('Enter values: ').split()]
    print('=' * 60)

    cho = input('Enter the value to insert: ')
    ch = int(cho) if cho.lstrip('-').isdigit() else cho
    print('=' * 60)

    n = int(input('Insert after every n-th element: '))
    print('=' * 60)

    result = []
    for i, val in enumerate(lst, start=1):
        result.append(val)
        if i % n == 0:
            result.append(ch)

except ValueError:
    print("Enter numeric value only.")

else:
    print(f"Original list: {lst}")
    print(f"Insert '{ch}' after every {n} elements: {result}")