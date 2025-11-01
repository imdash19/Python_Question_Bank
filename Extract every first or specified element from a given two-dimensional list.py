# Write a Python program to extract every first or specified element from a given two-dimensional list.
# Original list of lists: [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# Extract every first element from the said given two-dimensional list: [1, 4, 7]
# Extract every third element from the said given two-dimensional list: [3, 6, 9]

n= int(input("Please enter how many inner list you want: "))
lst= []
for i in range(n):
    print("="*60)
    print(f"Inside {n+1} inner list")
    print("="*60)
    ilst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(ilst)

i= int(input("Please enter the index to get elements: "))
print("="*60)
olst= []
for val in lst:
    olst.append(val[i-1])
print(f"""Original list of lists: {lst}
Extract every {i} element from the said given two-dimensional list: {olst}""")