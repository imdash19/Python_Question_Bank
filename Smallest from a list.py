#Write a PYTHON program to get the smallest number from a list.

n=int(input("Please enter how many numbers you want to enter: "))
print("You have entered {}".format(n))
lst=[]
small=0

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1, n+1):
        value=float(input("Enter {} value: ".format(i)))
        lst.append(value)

    for num in lst:
        if(small>=num):
            small=num
        else:pass

print("Smallest in {} is {}".format(lst, small))
print("Program executed successfully")