# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).

def sum_of_container():
    print("Choose container type:")
    print("1. List")
    print("2. Tuple")
    print("3. Set")
    print("4. Dictionary")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        data = list(map(int, input("Enter list elements separated by space: ").split()))
        print("Sum of list items:", sum(data))

    elif choice == 2:
        data = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
        print("Sum of tuple items:", sum(data))

    elif choice == 3:
        data = set(map(int, input("Enter set elements separated by space: ").split()))
        print("Sum of set items:", sum(data))

    elif choice == 4:
        n = int(input("Enter number of key-value pairs: "))
        d = {}
        for i in range(n):
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            d[key] = value
        print("Sum of dictionary values:", sum(d.values()))

    else:
        print("Invalid choice!")

sum_of_container()