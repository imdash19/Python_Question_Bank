# 	Write a Python program to calculate the average of a given list, after mapping each element to a value using the provided function.
# Sample Output: 5.0
#    15.0

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = input("Enter element: ")
    lst.append(value)
avg_len = sum(map(len, lst)) / len(lst)
nums = list(map(int, lst))
avg_sum = sum(nums) / len(nums)

print(avg_len)
print(avg_sum)