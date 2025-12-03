#  Write a Python program to convert a given list of strings into list of lists.
# Original list of strings: ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists: [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

try:
    lst= [val for val in input("Please enter your values separated with space: ").split()]
    print("="*60)
    slst= []
    for val in lst:
        ilst= []
        for i in val:
            ilst.append(i)
        slst.append(ilst)

except Exception:
    print("Something went wrong! Try again later...")

else:
    print(f"""Original list of strings: {lst}
Convert the said list of strings into list of lists: {slst}""")