#Write a PYTHON program to select the odd items of a list.

lst = [ele for ele in input("Please enter a single word: ") if len(ele) == 1]
print("-"*50)

print(lst)
print("-"*50)

rlst = [val for idx, val in enumerate(lst) if(idx % 2 == 1)]

print(rlst)
print("-"*50)

print("Program executed successfully")