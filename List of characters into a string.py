#Write a PYTHON program to convert a list of characters into a string.

n=int(input("Please enter how many list elements you want: "))
lst=[]
print("-"*30)

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

print("-"*30)
print(lst)
print("-"*30)

for ele in lst:
    print(ele, end=" ")


print("Program executed successfully")