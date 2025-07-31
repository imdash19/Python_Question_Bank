#Write a PYTHON program to convert a list of multiple integers into a single integer.
		# Sample list: [11, 33, 50]
		# Expected Output: 113350

import functools

lst = [int(val) for val in input("Please enter list of integers with space: ").split() if int(val) > 0]
print("-"*50)

print(lst)
print("-"*50)

res = functools.reduce(lambda a, b : str(a)+ "" +str(b), lst)
print("List of integers after converting into single integer: ",res)
print("-"*50)
print("Program executed successfully")