# Write a PYTHON program to count number of lists in a given list of lists.
# 		Original list: [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		Number of lists in said list of lists: 4
# 		Original list: [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# 		Number of lists in said list of lists: 3

try:
    lst = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
    print("-"*70)
    cnt = 0

    for ele in lst:
        cnt += 1

except Exception as e:
    print("-" * 70)
    print("Something went wrong! Please check again. ", e)
    print("-" * 70)

else:
    print("Original list: ", lst)
    print("-" * 70)
    print("Number of lists in said list of lists: ", cnt)
    print("-" * 70)

finally:
    print("Program executed successfully.")