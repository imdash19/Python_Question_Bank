# Write a PYTHON program to convert a string to a list.

lst = [word for word in input("Please enter your line of text: ").split()]
print("-"*70)

if(len(lst) == 0):
    print("Please enter a valid input")
    print("-" * 70)

else:
    print(lst)
    print("-" * 70)

print("Program executed successfully")