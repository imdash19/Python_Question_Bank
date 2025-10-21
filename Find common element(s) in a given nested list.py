# Write a Python program to find common element(s) in a given nested list.
# Original lists: [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
# Common element(s) in nested lists: [18, 12]

n = int(input("Please enter how many inner lists you want: "))
print("-" * 60)
lst = []
for i in range(n):
    ilst = [int(val) for val in input(f"Please enter {i+1} inner list value separated with space: ").split()]
    print("-" * 60)
    lst.append(ilst)

olst = []
for val in lst[0]:
    if val not in olst:
        olst.append(val)

elst = []
for val in olst:
    count = 0
    for i in lst:
        if val in i:
            count += 1
    if count == len(lst):
        elst.append(val)

print(f"""Original lists: {lst}
Common element(s) in nested lists: {elst[::-1]}""")