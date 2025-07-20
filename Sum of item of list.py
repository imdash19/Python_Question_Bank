#Write a PYTHON program to sum all the items in a list. 

n=int(input("Please enter how many numbers you want to enter:"))
print("You have entered {}".format(n))
lst=[]

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1, n+1):
        value=float(input("Please enter {} value:".format(i)))
        lst.append(value)
    
print("List = {} \n Sum of list elements = {}".format(lst, sum(lst)))