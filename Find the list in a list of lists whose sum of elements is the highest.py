# Write a PYTHON program to find the list in a list of lists whose sum of elements is the highest.
# 	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 	Expected Output: [10, 11, 12]

try:
    mlst = []
    n = int(input("Please enter how many inner list you want to enter: "))
    print("-" * 70)

    if(n <= 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        lst = []
        Max = 0
        for i in range(1, n+1):
            sublst = [int(val) for val in input("Please enter your lst values with space: ").split()]
            print("-" * 70)
            lst.append(sublst)

        for ele in lst:
            if(Max <= sum(ele)):
                Max = sum(ele)
                mlst = ele

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! please check again.", e)
    print("-" * 70)

else:
    print(mlst)
    print("-"*70)

finally:
    print("Program executed successfully")