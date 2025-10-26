# Write a Python program to iterate over all pairs of consecutive items in a given list.
# Original lists: [1, 1, 2, 3, 3, 4, 4, 5]
# Iterate over all pairs of consecutive items of the said list: [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("="*60)
olst= []
for i in range(len(lst)-1):
    tup= (lst[i], lst[i+1])
    olst.append(tup)
print(f"""Original lists: {lst}
Iterate over all pairs of consecutive items of the said list: [{olst}""")