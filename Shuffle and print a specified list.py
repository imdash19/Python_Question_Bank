#Write a PYTHON program to shuffle and print a specified list.

n=int(input("Please enter how many list elements you want: "))
print("You have entered {}".format(n))
lst=[]
print("-"*40)

if(n<=1):
    print("Please enter a value greater than 1")

else:
    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

print("List = ",lst)
print("-" * 40)

lst1=set(lst)
print(list(lst1))