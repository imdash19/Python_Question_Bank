#  Write a Python program to remove the last N number of elements from a given list.
# Original lists: [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# Remove the last 3 elements from the said list: [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# Remove the last 5 elements from the said list: [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
# Remove the last 1 element from the said list: [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]

def remove_element(olst, n):
    if len(olst) >= n:
        for _ in range(n):
            olst.pop()
    else:
        print('Sorry boss! List does not contain enough elements!')
    print('=' * 60)
    return olst


while True:
    try:
        lst = [int(val) if (val.lstrip('-')).isdigit() else val for val in input('Please enter your values separated with space: ').split()]
        print('=' * 60)

        n = int(input('Please enter how many elements you want to remove: '))
        print('=' * 60)

        olst= lst.copy()
        remove_element(olst, n)
        print(f"Original list: {lst}")
        print(f"Remove the last {n} elements: {olst}")
        print('=' * 60)

        print('''1. Do you want to remove custom N elements
2. Exit''')

        ch = int(input('Please enter your choice: '))
        print('=' * 60)

        match ch:
            case 1:
                olst = lst.copy()
                n = int(input('Please enter how many elements you want to remove: '))
                print('=' * 60)
                print(f"After removing given elements: {remove_element(olst, n)}")

            case 2:
                break

            case _:
                print('Invalid choice')

    except ValueError:
        print('Invalid input! Please enter a valid number...')

    except Exception:
        print('Something went wrong! Try again later...')