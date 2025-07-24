#Write a PYTHON program to get the difference between the two lists.

n=int(input("Please enter how many elements do you want in list1: "))
lst1=[]

if(n<=0):
    print("Please enter a valid input")

else:
    print("-"*50)
    for i in range(1, n+1):
        value1=input("Enter {} value: ".format(i))
        lst1.append(value1)

print("-"*50)
print(lst1)
print("-"*50)
m=int(input("Please enter how many elements do you want in list2:  "))
lst2=[]

if(m<=0):
    print("Please enter a valid input")

else:
    for j in range(1, m+1):
        value2=input("Enter {} value: ".format(j))
        lst2.append(value2)

print("-"*50)
print(lst2)
print("-"*50)

lst3=[]
for ele in lst1:
    if(ele in lst2):
        lst3.append(ele)

print("Common elements in {} & {} are {}".format(lst1, lst2, lst3))
print("Program executed successfully")