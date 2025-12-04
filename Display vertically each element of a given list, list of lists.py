#  Write a Python program to display vertically each element of a given list, list of lists.
# Original list: ['a', 'b', 'c', 'd', 'e', 'f']
# Display each element vertically of the said list:
# a
# b
# c
# d
# e
# f
# Original list: [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
# Display each element vertically of the said list of lists:
# 1 4 7
# 2 5 3
# 5 8 6

try:
    print("""1. One list
    2. List in list""")
    print("="*60)
    ch= input("Please enter your choice: ")
    print("="*60)

    match ch:
        case '1':
            lst= [int(val) if (val.lstrip('-')).isdigit() else val
                  for val in input("Please enter your values separated with space: ").split()]
            print("="*60)
            print(f"""Original list: {lst}
        Display each element vertically of the said list: """)
            for val in lst:
                print(val)

        case '2':
            i= int(input("Please enter how many inner list you want: "))
            print("="*60)

            lst= []
            for a in range(i):
                ilst= [int(val) if (val.lstrip('-')).isdigit() else val
                       for val in input("Please enter your values separated with space: ").split()]
                lst.append(ilst)

            print("="*60)
            print(f"""Original list: {lst}
        Display each element vertically of the said list of lists: """)

            for col in range(len(lst[0])):
                for row in range(len(lst)):
                    print(lst[row][col], end=" ")
                print()

        case _:
            print("Please enter a valid choice")

except Exception:
    print("Something went wrong! Try again later!")