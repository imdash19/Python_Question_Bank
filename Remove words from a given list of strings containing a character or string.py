# Write a Python program to remove words from a given list of strings containing a character or string.
# Original list: list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
# Character list: ['#', 'color', '@']
# New list: ['Red', '', 'Green', 'Orange', 'White']

lst = [val for val in input("Please enter your values separated with comma: ").split()]
print("-" * 60)
clst = [val for val in input("Please enter your list of values you want to remove separated with space: ").split()]
print("-" * 60)

nlst = []

for le in lst:
    temp = le
    for val in clst:
        if val in temp:
            temp = temp.replace(val, "")
    nlst.append(temp.strip())

print(f"""Original list: {lst}
Character list: {clst}
New list: {nlst}""")