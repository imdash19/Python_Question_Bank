#Write a PYTHON program to find the second-smallest number in a list.

n = int(input("Please enter how many list elements you want: "))
lst = []
slst=[]
print("-"*50)

if(n <= 1):
    print("Please enter above 1")

else:
    for i in range(1, n+1):
        value = int(input("Enter {} value: ".format(i)))
        lst.append(value)

    slst=lst.copy()
    lst.sort()

    print("Second-smallest in {} is {}".format(slst, lst[1]))

print("Program executed successfully")