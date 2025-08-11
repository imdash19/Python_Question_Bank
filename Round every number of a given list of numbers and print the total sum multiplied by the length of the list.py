#Write a PYTHON program to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result: 243

try :
    lst = [float(val) for val in input("Please enter your values separated with space: ").split()]
    print("-"*70)
    rlst = []
    for ele in lst:
        rlst.append(int(ele))

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again. ", e)
    print("-" * 70)

else:
    print("Original list: ", lst)
    print("-" * 70)
    print("Result: ",sum(rlst))
    print("-" * 70)

finally:
    print("Program executed successfully")