#Write a PYTHON program access the index of a list.

n=int(input("Please enter how many list elements you want: "))
lst=[]
print("-"*50)

if(n<=0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

    print(lst)
    print("-" * 50)

    m=int(input("Enter the index value to get the value: "))
    print("-" * 50)

    if(m >= len(lst) or m < -len(lst)):
        print("Please enter a valid index number")
        print("-" * 50)

    else:
        print("Index of {} in {} is {}".format(m, lst, lst[m]))
        print("-" * 50)

print("Program executed successfully")