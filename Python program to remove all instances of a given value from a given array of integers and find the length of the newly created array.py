# Write a Python program to remove all instances of a given value from a given array of integers and find the length of the newly created array.
# Sample Input:
# ([1, 2, 3, 4, 5, 6, 7, 5], 5)
# ([10,10,10,10,10], 10)
# ([10,10,10,10,10], 20)
# ([], 1)
# Sample Output:
# 6
# 0
# 5
# 0

s = input().strip()

a, v = s.split("],")
a = list(map(int, a.strip("([] ").split(",")))
v = int(v.strip(" )"))

b = []
for i in a:
    if i != v:
        b.append(i)

print(len(b))