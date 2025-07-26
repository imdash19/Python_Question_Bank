#Write a PYTHON program to find the second-largest number in a list.

n = int(input("Please enter how many elements you want to enter: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input: ")
    print("-" * 50)

else:
    lst=[]
    for i in range(1, n+1):
        value=int(input("Enter {} value: ".format(i)))
        lst.append(value)

    tlst=lst.copy()
    print("-" * 50)

    lst.sort(reverse=True)
    print("Second largest in {} is {}".format(tlst, lst[1]))

print("Project executed successfully")