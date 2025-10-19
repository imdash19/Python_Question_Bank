# Write a Python program to remove a specified column from a given nested list.
# Original Nested list: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column: [[2, 3], [4, 5], [1, 1]]
# Original Nested list: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# After removing 3rd column: [[1, 2], [-2, 4], [1, -1]]

lst= []
r= int(input("Please enter how many inner list you want: "))
print('-'*60)
c= int(input("Please enter how many elements you want in each list: "))
print('-' * 60)
for i in range(r):
    ilst= []
    print("Enter {} inner list elements".format(i+1))
    print('-' * 60)
    for j in range(c):
        e= int(input("Please enter {} element: ".format(j+1)))
        ilst.append(e)
    lst.append(ilst)
    print("-"*60)
rc= int(input("Please enter which column you want to remove: "))
print('-' * 60)
if rc > c:
    print("Invalid column selection try again!")
else:
    print("Original Nested list: ", lst)
    rc1= rc-1
    for i in lst:
        i.pop(rc1)
    print("After removing column no {}: {}".format(rc, lst))