# Write a Python program to swap two sub lists in a given list.
# Original list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Swap two sub lists of the said list: [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
# Swap two sub lists of the said list: [0, 9, 3, 8, 6, 7, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]

def swap_sublists(lst, s1, e1, s2, e2):
    return (
        lst[:s1] +
        lst[s2:e2+1] +
        lst[e1+1:s2] +
        lst[s1:e1+1] +
        lst[e2+1:]
    )


try:
    lst = [int(val) for val in input(
        "Enter list values separated with space: ").split()]
    print("=" * 60)

    s1 = int(input("Enter first sublist start index: "))
    e1 = int(input("Enter first sublist end index: "))
    s2 = int(input("Enter second sublist start index: "))
    e2 = int(input("Enter second sublist end index: "))
    print("=" * 60)

except ValueError:
    print("Please enter valid integers only")

except Exception:
    print("Something went wrong! Please try again...")

else:
    print(f'''Original list: {lst}
    Swap two sub lists of the said list:
    {swap_sublists(lst, s1, e1, s2, e2)}''')
