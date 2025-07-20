#Write a PYTHON program to remove duplicates from a list.

n=int(input("Enter how many elements do yo want to enter: "))
set1=set()
lst=[]

if(n<0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=input("Enter {} value: ".format(i))
        set1.add(value)
    lst=list(set1)

print(lst)
print("Program executed successfully")