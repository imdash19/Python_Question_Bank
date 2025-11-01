# Write a Python program to remove empty lists from a given list of lists.
# Original list: [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# After deleting the empty lists from the said lists of lists: ['Red', 'Green', [1, 2], 'Blue']

lst= [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
print(f"Original list: {lst}")
olst= []
for i in lst:
    if len(i) != 0:
        olst.append(i)
print(f"After deleting the empty lists from the said lists of lists: {olst}")