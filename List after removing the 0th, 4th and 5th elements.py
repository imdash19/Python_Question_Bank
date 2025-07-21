#Write a PYTHON program to print a specified list after removing the 0th, 4th and 5th elements.
		# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
		# Expected Output : ['Green', 'White', 'Black']
from operator import index

n=int(input("Please enter how many inputs you want: "))
lst=[]
if(n<=0):
    print("Please enter a valid input")

else:
    for i in range(1,n+1):
        value=input("Please enter {} word: ".format(i))
        lst.append(value)
    print("List = {}".format(lst))

    tlst=lst.copy()

    for val in lst:
        if(lst.index(val) in [0, 4, 5]):
            tlst.remove(val)

print("List after removing the 0th, 4th and 5th elements: {}".format(tlst))

print("Program executed successfully")