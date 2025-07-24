#Write a PYTHON program access the index of a list.

n=int(input("Please enter how many list elements you want: "))
lst=[]

if(n<=0):
    print("Please enter a valid input")

else:
    print("Enter elements of list")
    print("-"*30)
    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

print("-"*30)
print(lst)
print("-"*30)

m=input("Enter the index of list you want: ")
print("-"*30)

if(m in lst):
    print("Index value of {} in {} is {}".format(m, lst, lst.index(m)))
else:
    print("{} is not in {}".format(m, lst))

print("-"*30)
print("Program executed successfully")