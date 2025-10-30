# Write a Python program to sort a given list of strings(numbers) numerically.
# Original list: ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

try:
    lst= [int(val) for val in input("Please enter your values separated with space: ").split()]

except ValueError:
    print("Please enter a valid integer")

else:
    print(f"""Original list: {lst}
Sort the said list of strings(numbers) numerically: {sorted(lst)}""")