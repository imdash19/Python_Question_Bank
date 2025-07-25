#Write a PYTHON program to flatten a shallow list.
        #lst = [1,2,3,[4,5],6,[7,8]]
        #flatten_list = [1,2,3,4,5,6,7,8]

n=int(input("Please enter how many list items you want: "))
lst=[]
lst2=[]
flst=[]
print("-"*50)

if(n<=0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    print("Outer list elements")
    print("-" * 50)

    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

    print(lst)
    print("-" * 50)

m=int(input("Please enter how many inner list you want:"))

if(m<=0):
    print("-" * 50)
    print("Please enter a valid input")
    print("-" * 50)

else:
    for j in range(1, m+1):
        ilst=[]

        print("-" * 50)
        print("Inner list elements")
        print("-"*50)

        o = int(input("Enter how many list elements you want: "))
        print("-" * 50)

        for k in range(1, o+1):
            value2=input("Enter {} element: ".format(k))
            ilst.append(value2)

        lst2.append(ilst)

    print(lst2)
    print("-" * 50)

combined=lst+lst2
print("List = ",combined)
print("-" * 50)

for item in combined:
    if isinstance(item, list):
        flst.extend(item)
    else:
        flst.append(item)

print("Flatten shallow list = ",flst)
print("Program executed successfully")