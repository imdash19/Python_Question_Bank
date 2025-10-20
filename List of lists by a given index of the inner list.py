# Write a Python program to sort a list of lists by a given index of the inner list. # Original list: [['Greyson Fulton', 98, 99], ['Brady Kent', 97, 96], ['Wyatt Knott', 91, 94], ['Beau Turnbull', 94, 98]] # Sort the said list of lists by a given index (Index = 0) of the inner list: [['Beau Turnbull', 94, 98], ['Brady Kent', 97, 96], ['Greyson Fulton', 98, 99], ['Wyatt Knott', 91, 94]] # Sort the said list of lists by a given index (Index = 2) of the inner list: [['Wyatt Knott', 91, 94], ['Brady Kent', 97, 96], ['Beau Turnbull', 94, 98], ['Greyson Fulton', 98, 99]]

def convert_value(val):
    try:
        if '.' in val:
            return float(val)
        return int(val)
    except ValueError:
        return val

n = int(input("Please enter how many lists you want: "))
m = int(input("Please enter how many elements in each inner list: "))
print("-" * 60)

lst = []
for i in range(n):
    print(f"Inside list {i + 1}")
    ilst = []
    for j in range(m):
        val = input(f"Enter element {j + 1}: ")
        ilst.append(convert_value(val))
    lst.append(ilst)
    print("-" * 60)

e = int(input("Please enter index of element to sort by: "))
print("-" * 60)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i][e] > lst[j][e]:
            lst[i], lst[j] = lst[j], lst[i]

print(f"List sorted by element index {e}: ")
for val in lst:
    print(val, end=" ")