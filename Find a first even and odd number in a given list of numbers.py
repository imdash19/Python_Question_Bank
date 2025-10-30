# Write a Python program to find a first even and odd number in a given list of numbers.
# Original list: [1, 3, 5, 7, 4, 1, 6, 8]
# First even and odd number of the said list of numbers: (4, 1)

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("="*60)
even= 0
odd= 0
for i in lst:
    if i%2 == 0:
        even= i
        break
for i in lst:
    if i % 2 != 0:
        odd= i
        break

print(f"""Original list: lst
First even and odd number of the said list of numbers: ({even}, {odd})""")