#Write a PYTHON program to remove duplicates from a list of lists.
		# Sample list: [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
		# New List: [[10, 20], [30, 56, 25], [33], [40]]

try:
    nlst = []
    lst = []

    n = int(input("Please enter how mnay inner list you want: "))
    print("-" * 70)

    if(n <= 0):
        print("Please enter a valid input.")

    else:
        for i in range(1, n+1):
            slst = [int(val) for val in input("Please enter your numbers separated with space: ").split()]
            print("-" * 70)
            lst.append(slst)

        for val in lst:
            if(val in nlst):
                pass
            else:
                nlst.append(val)

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! please check again.", e)
    print("-" * 70)

else:
    print(nlst)
    print("-"*70)

finally:
    print("Program executed successfully.")