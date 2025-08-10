# Write a PYTHON program to decode a run-length encoded given list.
# 	Original encoded list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Decode a run-length encoded said list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]

try:
    lst = []
    n = int(input("Please enter how many inner list you want: "))
    print("-" * 70)

    if(n < 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        dlst = []
        for i in range(1, n+1):
            print("Inside {} inner list".format(i))
            print("-" * 70)
            m = int(input("Please enter the number of iteration: "))
            print("-" * 70)
            s = input("Please enter the letter: ")
            print("-" * 70)
            dlst.append([m, s])

    if(n > 0):
        for val in dlst:
            if(val[0] > 1):
                elst = []
                for j in range(1, val[0] + 1):
                    elst.append(val[1])
                lst.append(elst)
            elif(val[0] == 1):
                lst.append(val[1])

            else:pass

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please try again.", e)
    print("-" * 70)

else:
    print(lst)
    print("-"*70)

finally:
    print('Program executed successfully')