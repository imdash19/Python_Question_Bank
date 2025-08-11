# Write a PYTHON program to create a multidimensional list (lists of lists) with zeros.
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

try:
    lst = []
    n = int(input("Please enter how many inner list you want: "))
    print("-"*70)
    m = int(input("Please enter how many inner list elements you want: "))
    print("-"*70)

    if(n == 0 or m == 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        for i in range(1, n+1):
            slst = []
            for j in range(1, m+1):
                slst.append(0)
            lst.append(slst)

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again.", e)
    print("-" * 70)

else:
    print(lst)
    print("-" * 70)

finally:
    print("Program executed successfully")