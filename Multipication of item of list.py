#Write a PYTHON program to multiply all the items in a list.

n=int(input("Please enter how many numbers do you want to enter:"))
print("You have entered {}".format(n))
lst=[]
mval=1

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)

    for num in lst:
        mval*=num

print("Multipication value of all the items in list = {}".format(mval))
print("Program executed successfully")