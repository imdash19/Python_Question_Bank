# Write a Python program to remove first specified number of elements from a given list satisfying a condition.
# Remove the first 4 number of even numbers from the following list:
# Original list: [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
# Remove first 4 even numbers from the said list: [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]

lst = list(map(int, input("Enter list elements (space separated): ").split()))
print("=" * 60)

slst = lst.copy()
count = 0

print("""1. Remove even numbers
2. Remove odd numbers
3. Remove a specific number""")
print("=" * 60)

ch = int(input("Please enter your choice: "))
n = int(input("How many elements to remove?: "))
print("=" * 60)

match ch:
    case 1:     # even numbers
        for x in slst:        # iterate on original copy
            if x % 2 == 0:
                lst.remove(x)
                count += 1
            if count == n:
                break

    case 2:     # odd numbers
        for x in slst:
            if x % 2 == 1:
                lst.remove(x)
                count += 1
            if count == n:
                break

    case 3:     # specific number
        val = int(input("Enter the number to remove: "))
        for x in slst:
            if x == val:
                lst.remove(x)
                count += 1
            if count == n:
                break

    case _:
        print("Invalid choice!")

print(f"Original list: {slst}")
print(f"Updated list after removing elements: {lst}")