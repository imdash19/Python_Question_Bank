# Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
# Original lists: [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
# Consecutive duplicate elements and their frequency: ([1, 2, 4, 5], [1, 3, 3, 4])

lst = [int(val) for val in input("Please enter your values separated with space: ").split()]
print("=" * 60)

olst = []
clst = []
cnt = 1

for i in range(len(lst) - 1):
    if lst[i] == lst[i + 1]:
        cnt += 1
    else:
        olst.append(lst[i])
        clst.append(cnt)
        cnt = 1

olst.append(lst[-1])
clst.append(cnt)

print(f"""Original lists: {lst}
Consecutive duplicate elements and their frequency: ({olst}, {clst})""")