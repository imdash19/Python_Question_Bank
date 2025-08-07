# Write a PYTHON program to create a list of empty dictionaries.

try:
    n = int(input("Please enter how many empty dictionaries you want: "))
    print("-" * 70)

    lst = []
    if(n <= 0):
        print("Please enter a valid input")

    else:
        for i in range(1, n+1):
            d = {}
            lst.append(d)

except ValueError:
    print("-" * 70)
    print("Please enter an inter.")
    print("-" * 70)

else:
    print(lst)
    print("-" * 70)

finally:
    print("Program executed successfully")