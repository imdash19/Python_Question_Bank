# Write a PYTHON program to flatten a given nested list structure.
# 		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# 		Flatten list:
# 		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

try:
    flst = []

    lst = [val for val in input("Please enter your values separated with space: ").split()]
    print("-" * 70)
    clst = lst.copy()

    n = int(input("Please enter how many sub list you want: "))
    print("-" * 70)

    if(n <= 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        for i in range(1, n+1):
            print("Inside {} sub list".format(i))
            print("-" * 70)
            slst = [val for val in input("Please enter your list elements separated with space: ").split()]
            print("-" * 70)
            
            flst.append(slst)
            clst.append(slst)

        print(clst)
        print("-" * 70)

        for val in flst:
            lst += val

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again. ", e)
    print("-" * 70)

else:
    print(lst)
    print("-" * 70)

finally:
    print("Program executed successfully.")
