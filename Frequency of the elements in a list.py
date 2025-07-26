#Write a PYTHON program to get the frequency of the elements in a list.
from itertools import count

n = int(input("Please enter how many elements you want to enter: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")

else:
    lst=[]
    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value.lower())

    print("-" * 50)
    print("List of elements you have entered {}".format(lst))
    print("-" * 50)

    d = {}
    for ele in lst:
        d[ele] = lst.count(ele)

    print("Frequency of the elements is {}".format(d))

print("Program executed successfully")