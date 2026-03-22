# Write a Python program to compute the sum of the negative and positive numbers in an array of integers and display the largest sum.
# Original array elements: {0, 15, 16, 17, -14, -13, -12, -11, -10, 18, 19, 20}
# Largest sum - Positive/Negative numbers of the said array: 105
# Original array elements: {0, 3, 4, 5, 9, -22, -44, -11}
# Largest sum - Positive/Negative numbers of the said array: -77

arr = list(map(int, input().split()))
pos_sum = 0
neg_sum = 0
for i in arr:
    if i > 0:
        pos_sum += i
    elif i < 0:
        neg_sum += i
print(max(pos_sum, neg_sum))