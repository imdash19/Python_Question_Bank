# Write a PYTHON program to create a 3X3 grid with numbers.
# 	3X3 grid with numbers:
# 	[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

try:
    lst = []
    for i in range(1, 4):
        print("Inside {} list: ".format(i))
        print("-" * 70)
        slst = [ele for ele in input("Please enter 3 elements: ").split()]
        print("-" * 70)

        if(len(slst) == 3):
            lst.append(slst)

        else:
            break

except Exception as e:
    print("-"*70)
    print("Something went wrong! Please try again.", e)
    print("-" * 70)

else:
    if(len(lst) == 3):
        print(lst)

    else:
        print("Invalid input, please try again.")

    print("-" * 70)

finally:

    print("Program executed successfully.")
