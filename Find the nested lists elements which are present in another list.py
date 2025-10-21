# Write a Python program to find the nested lists elements which are present in another list.
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#                 [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists: [[12], [7, 11], [1, 5, 8]]

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
olst= []
m= int(input("Please enter how many inner list you want: "))
for i in range(m):
    print("-" * 60)
    slst= [int(val) for val in input(f"Please enter your {i+1} inner list values separated with space: ").split()]
    print("-" * 60)
    olst.append(slst)
ilst= []
for i in olst:
    elst= []
    for j in i:
        if j in lst:
            elst.append(j)
    ilst.append(elst)
print(f"""Original lists: {lst}
        {olst}
Intersection of said nested lists: {ilst}""")