# Write a Python program that determines the difference between the largest and smallest integers created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
# Input:
# Input an integer created by 8 numbers from 0 to 9.: 2345
# Difference between the largest and the smallest integer from the given integer: 3087

n = input()

small = int("".join(sorted(n)))
large = int("".join(sorted(n, reverse=True)))

print("Difference between the largest and the smallest integer from the given integer:", large - small)