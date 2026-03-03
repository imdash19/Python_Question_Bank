# Write a Python program to find the maximum sum of a contiguous subsequence from a given sequence of numbers a1, a2, a3, ... an. A subsequence of one element is also a continuous subsequence.
# Input: You can assume that 1 <= n <= 5000 and -100000 <= ai <= 100000.
# Input numbers are separated by a space.
# Input 0 to exit.
# Input number of sequence of numbers you want to input (0 to exit): 3
# Input numbers:
# 2
# 4
# 6
# Maximum sum of the said contiguous subsequence: 12
# Input number of sequence of numbers you want to input (0 to exit): 0

def max_subsequence_sum():
    while True:
        n = int(input("Input number of sequence of numbers you want to input (0 to exit): "))
        if n == 0:
            break
        nums = []
        print("Input numbers:")
        for _ in range(n):
            nums.append(int(input()))
        max_current = max_global = nums[0]
        for i in range(1, n):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)
        print("Maximum sum of the said contiguous subsequence:", max_global)

max_subsequence_sum()