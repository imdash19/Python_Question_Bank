#Write a PYTHON program to append a list to the second list.

n = int(input("Please enter how many lists you want: "))
lst = []

if(n <= 0):
    print("-" * 50)
    print("Please enter a valid input")
    print("-" * 50)

else:
    for i in range(1, n+1):
        ilst = []

        print("-" * 50)
        print("List {}".format(i))
        print("-" * 50)

        m=int(input("Enter how many list element you want: "))
        print("-" * 50)

        if(m<=0):
            print("Please enter a valid input")
            print("-" * 50)

        else:
            for j in range(1, m+1):
                value=input("Enter {} element: ".format(j))
                ilst.append(value)

            lst.append(ilst)

    print("List = ",lst)
    print("-" * 50)
print("Program executed successfully")