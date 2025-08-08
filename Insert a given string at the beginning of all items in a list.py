#Write a PYTHON program to insert a given string at the beginning of all items in a list.
	# Sample list: [1,2,3,4], string: emp
	# Expected output: ['emp1', 'emp2', 'emp3', 'emp4']

try:
    elst = []
    lst = [int(val) for val in input("Please enter your numbers with space: ").split()]
    print("-" * 70)

    if(len(lst) == 0):
        print("Please enter a valid input.")
        print("-" * 70)

    else:
        s = input("Please enter your string: ")
        print("-" * 70)

        for val in lst:
            value = s + str(val)
            elst.append(value)

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ",v)
    print("-" * 70)

except:
    print("-" * 70)
    print("Something went wrong! please check again.")
    print("-"*70)

else:
    print(elst)
    print("-" * 70)

finally:
    print("Program executed successfully")