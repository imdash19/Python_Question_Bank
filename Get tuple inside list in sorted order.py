#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
n=int(input("Please enter how many list elements you want to enter: "))
print("You have entered {}".format(n))
lst1=[] #[(1,3),(1,2),(1,4)]
lst3=[]
lst4=[]
if(n<=0):
    print("Please enter a valid input")
else:
    for i in range(1,n+1):
        lst2=[]
        v=int(input("Enter how many Tuple elements you have:"))
        for val in range(1,v+1):
            value = int(input("Enter {} value: ".format(val)))
            lst2.append(value)
            tobj=tuple(lst2)
        lst1.append(tobj)
    for j in lst1:
        lst3.append(j[-1])
    lst3.sort()
    for k in lst3:
        for l in lst1:
            if k==l[-1]:
                lst4.append(l)
    print(lst4)