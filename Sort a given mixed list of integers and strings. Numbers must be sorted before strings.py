# Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

lst= [val for val in input("Please enter your values separated by space: ").split()]
print("-"*60)
ilst= []
slst= []
for i in lst:
    if i.isdigit():
        ilst.append(i)
    else:
        slst.append(i)

print(f"""Original list: {lst}
Sort the said mixed list of integers and strings: {sorted(ilst) + sorted(slst)}""")