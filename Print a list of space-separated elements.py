# Write a PYTHON program to print a list of space-separated elements

lst = [val for val in input("Please enter your line of text: ").split()]
print("-"*70)

if(len(lst) == 0):
    print("Please enter a valid input")

else:
    print(lst)
    print("-"*70)

print(lst)