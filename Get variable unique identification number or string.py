#Write a PYTHON program to get variable unique identification number or string.
from operator import index

n = int(input("Please enter how many list elements you want: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst = []
    for i in range(1, n+1):
        value = input("Enter {} value: ".format(i))
        lst.append(value)

    print("List you have entered: ", lst)
    print("-" * 50)

    num = input("Please enter the element whose unique identification number you want: ")
    print("-" * 50)

    if(len(num) == 0):
        print("Please enter the element value")
        print("-" * 50)

    elif num.lower() in lst:
        print("Unique identification number of {} is {}".format(num, id(num)))
        print("-" * 50)

    else:
        print("Entered value not present in list you have entered")
        print("-"*50)

print("Program executed successfully")