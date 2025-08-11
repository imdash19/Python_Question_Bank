#Write a PYTHON program to generate the combinations of n distinct objects taken from the elements of a given list.
# HINT
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]

try:
    from itertools import combinations
    lst = [ele for ele in input("Please enter your elements separated with space: ").split()]
    print("-"*70)
    n = int(input("Please enter how many elements combination you want: "))
    print("-" * 70)
    combs = []

    if(n <= 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        combs = list(combinations(lst, n))

except ValueError as v:
    print("-" * 70)
    print("Please enter a valid input: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again. ", e)
    print("-" * 70)

else:
    print("Original list: ", lst)
    print("-" * 70)
    print("Combinations of {} distinct objects:". format(n))

    for c in combs:
        print(list(c), end="")
    print("-" * 70)

finally:
    print("Program executed successfully")