#Write a PYTHON program to get the largest number from a list.

n=int(input("Please enter how many numbers do you want to enter:"))
print("You have entered {}".format(n))
lst=[]
large=0

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)

    for num in lst:
        if(num>=large):
            large=num
        else:pass

print("Largest in {} is {}".format(lst, large))
print("Program executed successfully")