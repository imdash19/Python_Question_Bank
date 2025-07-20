#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#		Sample List : ['abc', 'xyz', 'aba', '1221']
#		Expected Result : 2

n=int(input("Please enter a number how many inputs you want to give: "))
print("You have entered {}".format(n))
lst=[]
count=0

if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=input("Enter {} value: ".format(i))
        lst.append(value)

    for ch in lst:
        if(ch[0]==ch[len(ch)-1]):
            count+=1

        else:pass

print("Number of strings matching the condition is {}".format(count))
print("Program executed successfully")
