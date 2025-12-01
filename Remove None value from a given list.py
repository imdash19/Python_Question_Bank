# Write a Python program to remove None value from a given list.
# Original list: [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list: [12, 0, 23, -55, 234, 89, 0, 6, -12]

try:
    lst= [int(val) if (val.lstrip("-")).isdigit() else val for val in input("Please enter your values separated with space: ").split()]
    print('='*60)
    slst= []
    for val in lst:
        if val is not None:
            slst.append(val)

except Exception as e:
    print(f"{e}! Try again later...")

else:
    print(f"""Original list: {lst}
Remove None value from the said list: {slst}""")