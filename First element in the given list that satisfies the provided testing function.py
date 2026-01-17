# 	Write a Python program to find the value of the first element in the given list that satisfies the provided testing function.
# Sample Output: 1
#     2

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

first_odd = next((x for x in lst if x % 2 != 0), None)
first_even = next((x for x in lst if x % 2 == 0), None)

print(first_odd)
print(first_even)