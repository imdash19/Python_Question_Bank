# Write a Python program to get all possible combinations of the elements of a given list.
# Original list: ['orange', 'red', 'green', 'blue']
# All possible combinations of the said list's elements: [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

from itertools import combinations

try:
    lst = input("Please enter your values separated with space: ").split()
    print("="*60)

except Exception:
    print("Something went wrong! Try again later....")

else:
    result = []

    for r in range(len(lst) + 1):
        for combo in combinations(lst, r):
            result.append(list(combo))

    print(f"""Original list: {lst}"
    All possible combinations of the said list's elements: {result}""")