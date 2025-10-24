# Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
# Original list: [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# Range: 8, 10
# Sum of the specified range: 29

lst = [int(val) for val in input("Please enter your values separated with space: ").split()]
print("-" * 60)
a = int(input("Please enter your starting range: "))
b = int(input("Please enter your ending range: "))
print("-" * 60)

sum_val = 0
for i in range(a, b + 1):
    sum_val += lst[i]

print(f"""Original list: {lst}
Range: ({a}, {b})
Sum of the specified range: {sum_val}""")