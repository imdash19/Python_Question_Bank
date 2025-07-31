#Write a PYTHON program to create multiple lists.

n = int(input("Please enter how many lists you want: "))

if(n <= 0):
    print("-" * 50)
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst = []

    for i in range(1, n+1):
        clst = []
        print("-" * 50)
        m = int(input("Please enter how many list elements you want in {}: ".format(i)))
        print("-" * 50)

        for j in range(1, m+1):
            value = input("Enter {} value: ".format(j))
            clst.append(value)

        lst.append(clst)

    for ele in lst:
        print(ele, end="")

print("\nProgram executed successfully")