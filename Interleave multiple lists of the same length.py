# Write a Python program to interleave multiple lists of the same length.
# Original list: list1: [1, 2, 3, 4, 5, 6, 7]
    #            list2: [10, 20, 30, 40, 50, 60, 70]
    #            list3: [100, 200, 300, 400, 500, 600, 700]
# Interleave multiple lists: [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]

n= int(input("Please enter how many lists you want: "))
lst= []
for i in range(n):
    print("="*60)
    print(f"Inside {i+1} list")
    print("="*60)
    slst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(slst)

print("Original list: ", end="")
for i in range(len(lst)):
    print(f"list{i+1}: {lst[i]}")

olst = []
for t in zip(*lst):
    for x in t:
        olst.append(x)

print(f"Interleave multiple lists: {olst}")