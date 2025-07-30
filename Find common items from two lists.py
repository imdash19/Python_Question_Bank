#Write a PYTHON program to find common items from two lists.

l1 = int(input("Please enter how many elements you want in list 1: "))
print("-"*50)

if(l1 <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst1 = []
    for i in range(1, l1 + 1):
        value = input("Enter {} value: ".format(i))
        lst1.append(value)

    print("-" * 50)

l2 = int(input("Please enter how many elements you want in list 2: "))
print("-" * 50)

if (l2 <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst2 = []
    for i in range(1, l1 + 1):
        value = input("Enter {} value: ".format(i))
        lst2.append(value)

    print("-" * 50)

lst3 = []
for ele in lst1:
    if ele in lst2:
        lst3.append(ele)

    else:pass

print("Common elements between {} & {} is {}".format(lst1, lst2, lst3))

print("Program executed successfully")