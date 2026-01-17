# 	Write a Python program to find the value of the last element in the given list that satisfies the provided testing function.
# Sample Output: 3
#     4

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

last_odd = next((x for x in reversed(lst) if x % 2 != 0), None)
last_even = next((x for x in reversed(lst) if x % 2 == 0), None)

print(last_odd)
print(last_even)