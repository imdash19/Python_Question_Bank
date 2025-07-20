#Write a PYTHON program to clone or copy a list.

n=int(input("Please enter how many list elements you want: "))
lst=[]
lst2=[]

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

    lst2=lst.copy()

print("Elements in list {} & copy is {}".format(lst, lst2))
print("Program executed successfully")