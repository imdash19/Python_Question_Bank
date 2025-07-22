#Write a PYTHON program to print the numbers of a specified list after removing even numbers from it.

n=int(input("Please enter how many numbers you want: "))
lst=[]

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=int(input("Enter {} value: ".format(i)))
        lst.append(value)
    print("List = {}".format(lst))

    for num in lst:
        if(num%2==0):
            lst.remove(num)

print("List after removing even numbers from it = {}".format(lst))