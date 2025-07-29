#Write a PYTHON program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

n = int(input("Please enter how many elements you want: "))
print("-"*50)

if(n <= 1):
    print("Please enter a valid input")

else:
    lst = []
    elst = []
    flst = []

    for i in range(1, n+1):
        value = int(input("Enter {} value: ".format(i)))
        lst.append(value)

    for j in lst[0:5] or lst[-5:]:
        elst.append(j)

    print("List of selected elements = ",elst)
    print("-"*50)

    for ele in elst:
        if((ele ** 0.5) in range(1, 31)):
            flst.append(ele)

    print("List of elements that satisfies the condition is ", flst)

print("Program executed successfully")