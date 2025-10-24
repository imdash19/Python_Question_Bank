# Write a Python program to count the same pair in three given lists.
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8]
# [2, 2, 3, 1, 2, 6, 7, 9]
# [2, 1, 3, 1, 2, 6, 7, 9]
# Number of same pair of the said three given lists: 3

n = int(input("Please enter how many lists you want: "))
lst = []

for i in range(n):
    print("=" * 60)
    print(f"Inside list {i + 1}")
    print("=" * 60)
    slst = [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(slst)

cnt = 0
for val in zip(*lst):
    if all(x == val[0] for x in val):
        cnt += 1

print("Original lists: ")
for i in range(n):
    print(f"List{i + 1}: {lst[i]}")

print("Number of same pair of the said three given lists: ", cnt)