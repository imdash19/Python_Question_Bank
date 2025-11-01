# Write a Python program to get the frequency of the elements in a given list of lists.
# Original list of lists: [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Frequency of the elements in the said list of lists: {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

n= int(input("Please enter how many inner list you want: "))
lst= []
for i in range(n):
    print("="*60)
    print(f"Inside {i+1} innerlist")
    print("="*60)
    ilst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(ilst)

print(f"Original list of lists: {lst}")
olst= []
for val in lst:
    for v in val:
        olst.append(v)

l= {}
for val in olst:
    l[val]= olst.count(val)
print(f"Frequency of the elements in the said list of lists: {l}")