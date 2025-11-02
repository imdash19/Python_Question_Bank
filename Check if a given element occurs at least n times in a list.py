# Write a Python program to check if a given element occurs at least n times in a list.
# Original list: [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
# Check if 3 occurs at least 4 times in a list: True
# Check if 0 occurs at least 5 times in a list: True
# Check if 8 occurs at least 3 times in a list: False

try:
    lst= [val for val in input("Please enter your list of elements separated with space: ").split()]
    print("="*60)
    e= input("Please enter the element: ")
    print("="*60)
    i= int(input("Please enter number of iterators you want: "))
    print("="*60)
    res= False
    if lst.count(e) == i:
        res= True

except ValueError:
    print("Don't enter CHARACTER / SPECIAL CHARACTER / NEGATIVE NUMBER as input...")

except Exception:
    print("Something went wrong! Please try again")

else:
    print(f"""Original list: {lst}
Check if 3 occurs at least 4 times in a list: {res}""")