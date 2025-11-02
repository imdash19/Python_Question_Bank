# Write a Python program to find the maximum and minimum values in a given list within specified index range.
# Original list: [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# Index range: 3 to 8
# Maximum and minimum values of the said given list within index range: (5, 0)

try:
    lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    print("="*60)
    s= int(input("Enter your starting index: "))
    e= int(input("Enter your ending index: "))
    print("="*60)

    slst= []
    for i in lst[s:e]:
        slst.append(i)

except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original list: {lst}
Index range: {s} to {e}
Maximum and minimum values of the said given list within index range: ({max(slst)}, {min(slst)})""")