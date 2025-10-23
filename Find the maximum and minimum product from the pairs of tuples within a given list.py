# Write a Python program to find the maximum and minimum product from the pairs of tuples within a given list.
# The original list, tuple: [(2, 7), (2, 6), (1, 8), (4, 9)]
# Maximum and minimum product from the pairs of the said tuple of list: (36, 8)

n= int(input("Please enter how many tuples you want in a list: "))
lst= []
olst= []
for i in range(n):
    print("-"*60)
    print(f"Inside {i+1} tuple")
    print("-"*60)
    tup= [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(tuple(tup))

    mx = 1
    for v in tup:
        mx *= v
    olst.append(mx)

print("The original list, tuple: ", lst)
print(f"Maximum and minimum product from the pairs of the said tuple of list: ({max(olst)}, {min(olst)})")