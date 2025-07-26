# Write a PYTHON program to count the number of elements in a list within a specified range.

n = int(input("Please enter how many elements you want to enter: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst = []
    blst = []

    for i in range(1, n+1):
        value = int(input("Please enter {} value: ".format(i)))
        lst.append(value)

    print("-" * 50)
    lower = int(input("Please enter the lower bond: "))
    print("-" * 50)
    upper = int(input("Please enter the upper bond: "))
    print("-" * 50)

    for ele in lst:
        if ele in range(lower, upper+1):
            blst.append(ele)

print("Elements in range from {} to {} in {} are {}".format(lower, upper, lst, blst))