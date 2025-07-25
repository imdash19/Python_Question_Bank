#Write a PYTHON program to check whether two lists are circularly identical.

n = int(input("Please enter how many list elements you want: "))
lst = []
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    for i in range(1, n+1):
        value1=input("Enter {} value: ".format(i))
        lst.append(value1)
        print("-" * 50)

    print(lst)
    print("-" * 50)

m = int(input("Please enter how many list elements you want: "))
lst2 = []
print("-"*50)

if (m <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    for j in range(1, m+1):
        value2 = input("Enter {} value: ".format(j))
        lst2.append(value2)
        print("-" * 50)

    print(lst2)
    print("-" * 50)

if(len(lst) != len(lst2)):
    print("Both lists are not circularly identical")
    print("-"*50)

else:
    if(lst[::-1] == lst2):
        print("Both lists are circularly identical")
        print("-" * 50)

    else:
        print("Both lists are not circularly identical")

print("Program executed successfully")