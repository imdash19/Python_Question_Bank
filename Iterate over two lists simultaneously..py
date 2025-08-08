# Write a PYTHON program to iterate over two lists simultaneously.
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 78]
# Expected output might be:
        # Alice: 85
        # Bob: 90
        # Charlie: 78

try:
    d = {}
    lst1 = [val for val in input("Please enter your list1 values with space: ").split()]
    print("-" * 70)

    lst2 = [val for val in input("Please enter your list2 values with space: ").split()]
    print("-" * 70)

    if(len(lst1) != len(lst2)):
        print("Both list doesn't have same length, please enter a valid input.")
        print("-" * 70)

    else:
        for val1, val2 in zip(lst1, lst2):
            d[val1] = val2

except Exception as e:
    print("-"*70)
    print("Something went wrong! please try again.", e)
    print("-" * 70)

else:
    for val1, val2 in d.items():
        print("{} : {}".format(val1, val2))

finally:
    print("Program executed successfully")