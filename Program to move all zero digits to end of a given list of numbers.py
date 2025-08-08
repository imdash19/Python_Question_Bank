# Write a PYTHON program to move all zero digits to end of a given list of numbers.
# 	Original list:
# 	[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# 	Expected output:
# 	[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
from itertools import count

try:
    elst = []
    lst = [int(val) for val in input("Please enter your list numbers with space: ").split()]
    print("-"*70)

    if(len(lst) == 0):
        print("Please enter a valid input: ")

    else:
        i = 1
        cnt = lst.count(0)

        for val in lst:
            if(val == 0):
                lst.remove(0)

        while(i <= cnt):
            elst.append(0)
            i += 1

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v, type(v))
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! please check again.", e, type(e))
    print("-" * 70)

else:
    print(lst + elst)
    print("-"*70)

finally:
    print("Program executed successfully.")