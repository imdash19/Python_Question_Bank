# Write a Python program to extract a specified column from a given nested list.
# Original Nested list: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column: [1, 2, 1]
# Original Nested list: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column: [3, -5, 1]

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
rc= int(input("Please enter which column you want to extract: "))
print('-' * 60)
if rc > c:
    print("Invalid column selection try again!")
else:
    olst= []
    print("Original Nested list: ", lst)
    rc1= rc-1
    for i in lst:
        o= i[rc1]
        olst.append(o)
    print("After extracting column no {}: {}".format(rc, olst))