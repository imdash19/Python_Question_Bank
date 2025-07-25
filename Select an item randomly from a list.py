#Write a PYTHON program to select an item randomly from a list.

n = int(input("Please enter how many list elements you want: "))
eset = set()
print("-" * 50)

if(n <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    for i in range(1, n+1):
        value = input("Enter {} value: ".format(i))
        print("-" * 50)
        eset.add(value)

    lst=list(eset)
    print("Randomly selected value is {}".format(lst[n-1]))

print("Program executed successfully")