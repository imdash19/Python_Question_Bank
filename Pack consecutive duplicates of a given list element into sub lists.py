#   Write a PYTHON program to pack consecutive duplicates of a given list element into sub lists.
# 	Original list:
# 	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 	After packing consecutive duplicates of the said list elements into sub lists:
# 	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

try:
    plst = []
    elst = []
    lst = [val for val in input("Please enter your numbers separated with space: ").split()]
    print("-"*70)

    if(len(lst) == 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        slst = []
        for i in range(0, len(lst)):
            if(lst[i] in slst):
                slst.append(lst[i])

            else:
                slst = []
                slst.append(lst[i])

            plst.append(slst)

        for i in range(0, len(plst)):
            if ((i < len(plst)-1) and (plst[i] != plst[i+1])):
                elst.append(plst[i])

except ValueError as v:
    print("-"*70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again. ", e)
    print("-" * 70)

else:
    print("After packing consecutive duplicates of the said list elements into sub lists: ", elst)
    print("-"*70)

finally:

    print("Program executed successfully")
