# Write a Python program to reverse a given list of lists.
# Original list: [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
# Reverse said list of lists: [['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
# Original list: [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]
# Reverse said list of lists: [[2, 3, 4, 2, 4], [0, 2, 4, 5], [1, 2, 3, 4]]

try:
    n = int(input("Please enter how many inner lists you want: "))
    lst = []

    if n <= 0:
        raise ValueError

    for i in range(n):
        print("="*60)
        print(f"Inside {i+1} inner list")
        print("="*60)
        raw = input("Please enter list values separated with space: ").split()
        inner_list = []
        for val in raw:
            if val.lstrip('-').isdigit():
                inner_list.append(int(val))
            else:
                inner_list.append(val)
        lst.append(inner_list)

except ValueError:
    print("Please don't enter ZERO / NEGATIVE NUMBER / CHARACTERS as input...")

except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original list: {lst}
Reverse said list of lists: {lst[::-1]}""")