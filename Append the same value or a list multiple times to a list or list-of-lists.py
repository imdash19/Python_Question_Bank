# Write a Python program to append the same value /a list multiple times to a list/list-of-lists.
# Add a value (7), 5 times, to a list: ['7', '7', '7', '7', '7']
# Add 5, 6 times, to a list: [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# Add a list, 4 times, to a list of lists: [[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
# Add a list, 3 times, to a list of lists: [[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]

print("""1. Append the same value 
2. Append a list multiple times to a list""")

ch = input("Please enter your choice (1/2): ")
print("=" * 60)

match ch:
    case "1":      # Append same value
        print("""a. Append the same value to a new list
b. Append the same value to an existing list""")

        ch2 = input("Please enter your choice (a/b): ")
        print("=" * 60)

        match ch2:
            case "a":
                lst = []
                a = input("Please enter your value: ")
                b = int(input("How many times to append? "))
                print("=" * 60)

                for _ in range(b):
                    lst.append(a)

                print(f"Add value {a}, {b} times → {lst}")

            case "b":
                lst = input("Enter existing list values (space separated): ").split()
                slst = lst.copy()
                a = input("Value to append: ")
                b = int(input("How many times to append? "))
                print("=" * 60)

                for _ in range(b):
                    lst.append(a)

                print(f"Add value {a}, {b} times to {slst} → {lst}")

            case _:
                print("Invalid choice! Please enter a/b.")

    case "2":      # Append list multiple times
        print("""a. Append the same list to a new list
b. Append the same list to an existing list""")

        ch2 = input("Please enter your choice (a/b): ")
        print("=" * 60)

        match ch2:
            case "a":
                lst = []
                a = input("Enter list values (space separated): ").split()
                b = int(input("How many times to append? "))
                print("=" * 60)

                for _ in range(b):
                    lst.append(a.copy())   # avoid reference issue

                print(f"Add list {a}, {b} times → {lst}")

            case "b":
                lst = input("Enter existing list values (space separated): ").split()
                slst = lst.copy()
                a = input("Enter list to append (space separated): ").split()
                b = int(input("How many times to append? "))
                print("=" * 60)

                for _ in range(b):
                    lst.append(a.copy())

                print(f"Add list {a}, {b} times to {slst} → {lst}")

            case _:
                print("Invalid choice! Please enter a/b.")

    case _:
        print("Invalid choice! Please enter 1 or 2.")