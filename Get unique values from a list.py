#Write a PYTHON program to get unique values from a list.

n = int(input("Please enter how many list elements you want: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")
    print("-"*50)

else:
    lst=[]
    for i in range(1, n+1):
        value = input("Enter {} element: ".format(i))
        lst.append(value)

    lset=set(lst)
    lst2=list(lset)
    print("Unique elements from {} is {}".format(lst, lst2))

print("Program executed successfully")