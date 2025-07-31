#Write a PYTHON program to change the position of every nth value with the (n+1) th in a list.
	# Sample list: [0,1,2,3,4,5]
	# Expected Output: [1, 0, 3, 2, 5, 4]

n = int(input("Please enter how many list elements you want: "))
print("-"*50)

if(n <= 0):
    print("Please enter a valid input")

else:
    lst = []
    for i in range(1, n+1):
        value = input("Enter {} value: ".format(i))
        lst.append(value)

    print("-" * 50)

print("List of values before swapping: ", lst)
print("-" * 50)

def swap_nth_with_next(slst, m):
    i = m - 1
    while i < len(slst) - 1:
        slst[i - 1], slst[i] = slst[i], slst[i - 1]
        i += m
    return slst

m = 2
res = swap_nth_with_next(lst, m)
print("List of values after swapping: ", res)
print("-" * 50)

print("Program executed successfully")















