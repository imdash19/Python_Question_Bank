# Write a PYTHON program to find missing and additional values in two lists.
# 	Sample data : Missing values in second list: b,a,c
# 	Additional values in second list: g,h

lst1 = {word for word in input("Please enter elements of list1 with space: ").split()}
print("-"*50)
print(lst1)
print("-"*50)

lst2 = {word for word in input("Please enter elements of list2 with space: ").split()}
print("-"*50)
print(lst2)
print("-"*50)

print("Missing values in list1 is: ", lst1.difference(lst2))
print("-"*50)

print("Additional values in list1 is: ", lst2.difference(lst1))
print("-"*50)

print("Program executed successfully")