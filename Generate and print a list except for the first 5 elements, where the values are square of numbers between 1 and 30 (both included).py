#Write a PYTHON program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

n = int(input("Please enter how many elements you want: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst = []
    elst = []
    flst = []

    for i in range(1, n+1):
        value = int(input("Enter {} value: ".format(i)))
        lst.append(value)
    print("-" * 50)

    for ele in lst[5:]:
        elst.append(ele)
    print("Selected elements from list is ", elst)
    print("-" * 50)

    for val in elst:
        if ((val ** 2) not in range(1, 31)):
            flst.append(val)

    print("List of elements that satisfies the condition is ", flst)

print("Program executed successfully")