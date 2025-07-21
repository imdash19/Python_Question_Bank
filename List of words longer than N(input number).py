#Write a PYTHON program to find the list of words that are longer than N from a given list of words.

n=int(input("Please enter how many inputs you want: "))
lst=[]
rest=[]

if (n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=input("Please enter {} word: ".format(i))
        lst.append(value)
    print("List = {}".format(lst))

    N=int(input("Please enter length: "))
    for length in lst:
        if (len(length)>N):
            rest.append(length)

        else:pass

    print("List of words longer than {} are {}".format(N,rest))

print("Program executed successfully")
