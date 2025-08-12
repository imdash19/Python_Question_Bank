# Write a PYTHON program to find the list with maximum and minimum length.

# 	Original list: [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 	List with maximum length of lists: (3, [13, 15, 17])
# 	List with minimum length of lists: (1, [0])

# 	Original list: [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists: (3, [3, 5, 7])
# 	List with minimum length of lists:(1, [0])

# 	Original list: [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists: (4, [1, 34, 5, 7])
# 	List with minimum length of lists: (1, [12])

try:
    lst = []
    n = int(input("Please enter how many inner list you want: "))
    print("-"*70)

    if(n <= 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        for i in range(1, n+1):
            slst = [ele for ele in input("Please enter your values separated with space: ").split()]
            print("-" * 70)
            lst.append(slst)

        lenlst = []
        maxl = []
        minl = []
        be = 0
        se = 0

        for ele in lst:
            lenlst.append(len(ele))

        for val in lst:
            if(max(lenlst) == len(val)):
                maxl.append((max(lenlst), val))

        for val in lst:
            if(min(lenlst) == len(val)):
                minl.append((min(lenlst), val))

except ValueError as v:
    print("-" * 70)
    print("Please enter a valid input: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again.", e)
    print("-" * 70)

else:
    print("Original list: ", lst)
    print("-" * 70)
    print("List with maximum length of lists: ", maxl)
    print("-" * 70)
    print("List with minimum length of lists: ", minl)
    print("-" * 70)

finally:
    print("Program executed successfully")