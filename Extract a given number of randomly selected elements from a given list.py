# Write a PYTHON program to extract a given number of randomly selected elements from a given list.
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Selected 3 random numbers of the above list:
# 	[4, 4, 1]

try:
    lst = [val for val in input("Please enter your elements separated with space: ").split()]
    print("-" * 70)
    print("Original list: ", lst)
    print("-" * 70)

    n = int(input("Please enter how many random elements you want: "))
    print("-" * 70)

    if(n >= 0):
        lset = set(lst)
        lst = list(lset)

    else:
        print("Please enter a number >= 0")
        print("-" * 70)

except ValueError as v:
    print("-"*70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-"*70)
    print("Something went wrong! Please check again.", e)
    print("-" * 70)

else:
    print("Selected 3 random numbers of the given list: ", lst[0:n])
    print("-" * 70)

finally:
    print("Program executed successfully")