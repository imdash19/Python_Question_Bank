#  Write a Python program to convert a given list of strings and characters to a single list of characters.
# Original list: ['red', 'white', 'a', 'b', 'black', 'f']
# Convert the said list of strings and characters to a single list of characters:
# ['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']

try:
    lst= [int(val) if (val.lstrip('-').isdigit()) else val for val in input('Please enter your values separated by space: ').split()]
    print("="*60)
    olst= []
    for val in lst:
        for i in val:
            olst.append(i)

except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original list: {lst}
     Convert the said list of strings and characters to a single list of characters: {olst}""")