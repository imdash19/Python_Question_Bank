# Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]

arr = list(map(int, input().strip('[]').split(',')))

result = []

for num in arr:
    s = str(num)

    if s[0] == '-':
        digit_sum = -int(s[1]) + sum(int(ch) for ch in s[2:])
    else:
        digit_sum = sum(int(ch) for ch in s)

    if digit_sum > 0:
        result.append(num)

print(result)