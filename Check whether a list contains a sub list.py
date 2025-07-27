# Write a PYTHON program to check whether a list contains a sub list.

n = int(input("Please enter how many list elements you want: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input.")
    print("-" * 50)

else:
    lst = []
    for i in range(1, n+1):
        value = input("Enter {} value: ".format(i))
        lst.append(value)
    print("-" * 50)

    s = input("Do you want inner list, please enter (Yes / No): ")
    print("-" * 50)

    if(s.lower() == "yes"):
        m = int(input("Please enter how many inner list you want: "))
        print("-" * 50)

        if(m <= 0):
            print("Please enter a valid input")
            print("-" * 50)

        else:
            for j in range(1, m+1):
                o = int(input("Please enter how many inner list elements you want: "))
                print("-" * 50)

                if(o < 0):
                    print("Please enter a valid input")
                    print("-" * 50)

                elif(o == 0):
                    elst = []
                    lst.append(elst)

                else:
                    lst2 = []
                    for k in range(1, o+1):
                        value3 = input("Please enter {} value: ".format(k))
                        lst2.append(value3)
                    lst.append(lst2)
                    print("-" * 50)

        print("There is inner list present inside the list")
        print("-" * 50)

    elif(s.lower() == "no"):
        print("There is no inner list present")
        print("-" * 50)

    else:
        print("Invalid input")
        print("-" * 50)

    print(lst)

print("Program executed successfully")