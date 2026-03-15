# Write a Python program to check whether a given sequence is linear, quadratic or cubic.
# Sequences are sets of numbers that are connected in some way.
# Linear sequence:
# A number pattern which increases or decreases by the same amount each time is called a linear sequence. The amount it increases or decreases by is known as the common difference.
# Quadratic sequence:
# In quadratic sequence, the difference between each term increases, or decreases, at a constant rate.
# Cubic sequence:
# Sequences where the 3rd difference are known as cubic sequence.
# Sample Output:
# Original Sequence: [0, 2, 4, 6, 8, 10]
# Check the said sequence is Linear, Quadratic or Cubic?
# Linear Sequence
# Original Sequence: [1, 4, 9, 16, 25]
# Check the said sequence is Linear, Quadratic or Cubic?
# Quadratic Sequence
# Original Sequence: [0, 12, 10, 0, -12, -20]
# Check the said sequence is Linear, Quadratic or Cubic?
# Cubic Sequence
# Original Sequence: [1, 2, 3, 4, 5]
# Check the said sequence is Linear, Quadratic or Cubic?
# Linear Sequence

s = eval(input())

d1 = []
for i in range(len(s)-1):
    d1.append(s[i+1] - s[i])

d2 = []
for i in range(len(d1)-1):
    d2.append(d1[i+1] - d1[i])

d3 = []
for i in range(len(d2)-1):
    d3.append(d2[i+1] - d2[i])

if len(set(d1)) == 1:
    print("Linear Sequence")
elif len(set(d2)) == 1:
    print("Quadratic Sequence")
elif len(set(d3)) == 1:
    print("Cubic Sequence")