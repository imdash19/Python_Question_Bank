# Write a PYTHON program to print a nested lists (each list on a new line) using the print() function.

n = int(input("Please enter how many inner list elements you want: "))
print("="*50)

if(n <= 0):
    print("Please enter a valid input")
    print("-"*50)

else:
    lst = []
    for i in range(1, n+1):
        ilst = [val for val in input("Please enter your elements using space: ").split()]
        lst.append(ilst)

    print("List you have entered: ",lst)
    print("-"*50)

    for inner_lst in lst:
        print(inner_lst)

print("Program executed successfully")