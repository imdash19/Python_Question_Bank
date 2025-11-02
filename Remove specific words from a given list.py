# Write a Python program to remove specific words from a given list.
# Original list: ['red', 'green', 'blue', 'white', 'black', 'orange']
# Remove words: ['white', 'orange']
# After removing the specified words from the said list: ['red', 'green', 'blue', 'black']

try:
    lst= [val for val in input("Please enter your values separated with space: ").split()]
    print("="*60)
    rlst= [val for val in input("Please enter your words to remove from list: ").split()]
    print("="*60)
    slst= []
    for val in lst:
        if val not in rlst:
            slst.append(val)

except Exception:
    print("Somrthing went wrong! Try again later.")

else:
    print(f"""Original list: {lst}
Remove words: {rlst}
After removing the specified words from the said list: {slst}""")