# Write a PYTHON program to check whether all dictionaries in a list are empty or not.
# 	Sample list: [{}, {}, {}]
# 	Return value: True
# 	Sample list: [{1,2}, {}, {}]
# 	Return value: False

try:
    lst = []
    result = True

    n = int(input("Please enter how many inner dictionaries you want: "))
    print("-" * 70)

    if(n <= 0):
        print("Please enter a valid input.")

    else:
        for i in range(1, n+1):
            d = {val for val in input("Please enter your inner dictionary elements: ").split()}
            print("-" * 70)
            lst.append(d)

        for item in lst:
            if(len(item) != 0):
                result = False
                break

            else:
                pass

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-"*70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again: ", e)
    print("-"*70)

else:
    print(result)
    print("-" * 70)

finally:
    print("Program executed successfully")