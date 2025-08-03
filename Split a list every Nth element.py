# Write a PYTHON program to split a list every Nth element.
# 	Sample list: [a b c d e f g h i j k l m n]
# 	Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

lst = [val for val in input("Please enter your values using space: ").split()]
print("-"*70)

if(len(lst) == 0):
    print("Please enter a value")
    print("-" * 70)

else:
    n = int(input("Please enter the value of N(split every Nth element): "))
    print("-"*70)

    if(n <= 0):
        print("Please enter a value")
        print("-" * 70)

    else:
        nlst = [lst[i::n] for i in range(n)]

        print(nlst)
        print("-" * 70)

print("Program executed successfully")