# Write a PYTHON program to generate groups of five consecutive numbers in a list.

lst = [int(val) for  val in input("Please enter the values with space: ").split()]
print("-"*50)

print(lst)
print("-"*50)

lst.sort()
res = lst[0:5]
print(res)
print("-"*50)

print("Program executed successfully")