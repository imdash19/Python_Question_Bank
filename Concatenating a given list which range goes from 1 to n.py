# Write a PYTHON program to create a list by concatenating a given list which range goes from 1 to n.
# 	Sample list: ['p', 'q']
# 	n =5
# 	Sample Output: ['p1', 'p2', 'p3', 'p4', 'p5', 'q1', 'q2', 'q3', 'q4', 'q5']

m = int(input("Please enter how many list elements you want: "))
print("-"*50)

if(m <= 0):
    print("Please enter a valid input")
    print("-" * 50)

else:
    lst = []
    clst = []
    for i in range(1, m+1):
        value1 = input("Enter {} element: ".format(i))
        lst.append(value1)

    print(lst)
    print("-" * 50)
    n = int(input("Please enter your range: "))
    print("-" * 50)

    if(n <= 0):
        print("Please enter a valid input")
        print("-" * 50)

    else:
        for ele in lst:
            for val in range(1, n+1):
                clst.append(ele + str(val))

        print(clst)
        print("-"*50)

print("Program executed successfully")