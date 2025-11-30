# Write a Python program to get the items from a given list with specific condition.
# Original list: [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Number of Items of the said list which are even and greater than 45: 5

try:
    lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    print("="*60)
    ch= int(input("Please enter your choice: "))
    print("="*60)
    slst= []
    for val in lst:
        if (val > ch) and (val % 2 == 0):
            slst.append(val)

except ValueError:
    print("Please enter a number. Try again...")

except Exception:
    print("Please enter a number. Try again later...")

else:
    print(f"""Original list: {lst}
Number of Items of the said list which are even and greater than {ch}: {len(slst)}""")