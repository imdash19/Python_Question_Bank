#Write a PYTHON program to check a list is empty or not.

n=int(input("Enter how many inputs you want: "))
lst=[]

if(n<0):
    print("Please enter a valid input")

else:
    for i in range(1, n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

        for element in lst:
            if(len(element)>0):
                Result="Not an empty list"
                break
            else:
                Result="Empty list"

print(Result)
print("Program executed successfully")