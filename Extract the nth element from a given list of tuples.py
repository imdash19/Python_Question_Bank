# Write a Python program to extract the nth element from a given list of tuples.
# Original list: [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Extract nth element (n = 0) from the said list of tuples: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# Extract nth element (n = 2) from the said list of tuples: [99, 96, 94, 98]

n= int(input("Please enter how many tuples you want: "))
m= int(input("Please enter how many tuple elements you want: "))
print("-"*60)
lst= []
for i in range(n):
    print(f"Inside {i+1} tuple")
    print("-" * 60)
    tup= []
    for j in range(m):
        t= input(f"Please enter your {j+1} value: ")
        tup.append(t)
    lst.append(tup)
    print("-" * 60)

e= int(input("Please enter index of element to extract from tuples: "))
print("-" * 60)
olst= []
elst= []
for val in lst:
    elst.append(val[e])
for val in lst:
    olst.append(tuple(val))
print("Original list: ", olst)
print(f"Extract nth element (n = {e}) from the said list of tuples: ", elst)