# Write a PYTHON program to Zip two given lists of lists.
# 	Original lists:
# 	[[1, 3], [5, 7], [9, 11]]
# 	[[2, 4], [6, 8], [10, 12, 14]]
# 	Zipped list: [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]

try:
    lst = []
    n = int(input("Please enter how many inner list you want in list 1: "))
    print("-" * 70)
    lst1 = []

    for i in range(1, n+1):
        print("Inside {} inner list:".format(i))
        print("-" * 70)
        ilst = [ele for ele in input("Please enter your elements separated with space: ").split()]
        print("-" * 70)
        lst1.append(ilst)

    m = int(input("Please enter how many inner list you want in list 2: "))
    print("-" * 70)
    lst2 = []

    for i in range(1, m+1):
        print("Inside {} inner list:".format(i))
        print("-" * 70)
        ilst = [ele for ele in input("Please enter your elements separated with space: ").split()]
        print("-" * 70)
        lst2.append(ilst)

    for i1, i2 in zip(lst1, lst2):
        lst.append(i1+i2)

except ValueError as v:
    print("-"*70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again.", e)
    print("-" * 70)

else:
    if(len(lst1) == len(lst2)):
        print("Original list: ",lst1, lst2)
        print("-" * 70)
        print("Zipped list: ",lst)
        print("-" * 70)

    else:
        print("Both the list doesn't have same number of inner list.")

finally:
    print("Program executed successfully.")