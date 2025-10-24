# Write a Python program to reverse each list in a given list of lists.
# Original list of lists: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Reverse each list in the said list of lists: [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]

n= int(input("Please enter how many inner list you want: "))
lst= []
for i in range(n):
    print("="*60)
    print(f"Inside {i+1} inner list")
    print("=" * 60)
    ilst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(ilst)
olst= []
for val in lst:
    ov= val[::-1]
    olst.append(ov)
print(f"""Original list of lists: {lst}
Reverse each list in the said list of lists: {olst}""")