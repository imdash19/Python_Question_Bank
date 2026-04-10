# Write a Python program to calculate the average of the numbers a through b (b not included) rounded to the nearest integer, in binary (or -1 if there are no such numbers).
# Input: 4, 7
# Output: 0b101
# Input: 11, 19
# Output: 0b1110

a, b = map(int, input().split(', '))

nums = list(range(a, b))

if not nums:
    print(-1)
else:
    avg = round(sum(nums) / len(nums))
    print(bin(avg))