# Write a PYTHON program to concatenate elements of a list.

lst = [val for val in input("Please enter your values with space: ").split()]
print("-"*70)
print(lst)
print("-"*70)

if(len(lst) == 0):
    print("Please enter a valid input")
    print("-"*70)

else:
    string = ""
    for ele in lst:
        string += ele

    print(string)
    print("-" * 70)


print("Program executed successfully")
