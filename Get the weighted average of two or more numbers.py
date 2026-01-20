# 	Write a Python program to get the weighted average of two or more numbers.
# Sample Output:
# Original list elements: [10, 50, 40]
#   [2, 5, 3]
# Weighted average of the said two list of numbers: 39.0
# Original list elements: [82, 90, 76, 83]
#   [0.2, 0.35, 0.45, 32]
# Weighted average of the said two list of numbers: 82.97272727272727

n = int(input("Enter number of elements: "))
values = []
print("Enter the values:")
for i in range(n):
    values.append(float(input(f"Value {i + 1}: ")))

weights = []
print("Enter the corresponding weights:")
for i in range(n):
    weights.append(float(input(f"Weight {i + 1}: ")))

weighted_sum = sum(v * w for v, w in zip(values, weights))
total_weight = sum(weights)
weighted_average = weighted_sum / total_weight
print("Original list elements:", values)
print(" ", weights)
print("Weighted average of the said two list of numbers:", weighted_average)