# Write a Python program to generate and print a list of numbers from 1 to 10.
# Sample Input:
# range(1,10)
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

nums = list(range(1, 10))
str_nums = [str(i) for i in nums]

print(nums)
print(str_nums)