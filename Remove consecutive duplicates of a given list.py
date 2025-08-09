# Write a PYTHON program to remove consecutive duplicates of a given list.
# 		Original list:
# 		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 		After removing consecutive duplicates:
# 		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

try:
    lst = [int(val) for val in input("Please enter your values separated with space: ").split()]
    print("-" * 70)
    print("Original list: ",lst)
    print("-"*70)
    slst = []

    for i in range(0, len(lst)):
        if(lst[i] != lst[i-1]):
            slst.append(lst[i])

except ValueError as v:
    print("-"*70)
    print("Please enter a number: ", v)
    print("-" * 70)

# except Exception as e:
#     print("-" * 70)
#     print("Something went wrong! Please try again.", e)
#     print("-" * 70)

else:
    print("After removing consecutive duplicates: ", slst)
    print("-"*70)

finally:
    print("Program executed successfully")