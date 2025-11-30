# Write a Python program to get the index of the first element which is greater than a specified element.
# Original list: [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# Index of the first element which is greater than 73 in the said list: 4
# Index of the first element which is greater than 21 in the said list: 1
# Index of the first element which is greater than 80 in the said list: 5
# Index of the first element which is greater than 55 in the said list: 3

try:
    lst= [int(val) if (val.lstrip("-")).isdigit() else val for val in input("Please enter your value separated with space: ").split()]
    print("="*60)
    ch= input("Please enter your choice: ")
    if (ch.lstrip("-")).isdigit():
        ch= int(ch)
    print("="*60)

except Exception:
    print("Something went wrong! Try again later...")

else:
    for val in lst:
        if val > ch:
            print(f"Index of the first element which is greater than {ch} in the said list: {lst.index(val)}")
            break