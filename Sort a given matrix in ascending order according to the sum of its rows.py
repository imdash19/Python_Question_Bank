# Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
# 	Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# 	Sort the said matrix in ascending order according to the sum of its rows: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# 	Original Matrix:: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# 	Sort the said matrix in ascending order according to the sum of its rows: [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
# Write a Python program to sort a given matrix in ascending order according to the sum of its rows.

i = int(input("Please enter how many inner list you want: "))
j = int(input("Please enter how many inner list elements you want: "))

lst = []
for a in range(i):
    print("-" * 60)
    print(f"Inside {a + 1} list: ")
    print("-" * 60)
    sl = []
    for b in range(j):
        le = int(input(f"Please enter {b + 1} element: "))
        sl.append(le)
    lst.append(sl)

print("Original matrix:", lst)

sum_list = []
for val in lst:
    sum_list.append(sum(val))

sorted_sums = sum_list[:]
sorted_sums.sort()

sorted_matrix = []
for s in sorted_sums:
    for val in lst:
        if sum(val) == s and val not in sorted_matrix:
            sorted_matrix.append(val)
            break

print("Sort the said matrix in ascending order according to the sum of its rows:", sorted_matrix)