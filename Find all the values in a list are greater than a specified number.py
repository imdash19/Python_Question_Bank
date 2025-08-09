# Write a PYTHON program to find all the values in a list are greater than a specified number.

try:
    lst = [int(val) for val in input("Please enter your values separated with space: ").split()]
    print("-" * 70)
    olst = []

    if(len(lst) == 0):
        print("Please enter a valid input.")

    else:
        n = int(input("Please enter your number: "))
        print("-" * 70)

        for val in lst:
            if(val > n):
                olst.append(val)

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! please check again.", e)
    print("-"*70)

else:
    print(olst)
    print("-"*70)

finally:
    print("program executed successfully")