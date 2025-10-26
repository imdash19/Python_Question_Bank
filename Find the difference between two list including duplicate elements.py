# Write a Python program to find the difference between two list including duplicate elements.
# Original lists: [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# [1, 1, 2, 4, 5, 6]
# Difference between two said list including duplicate elements: [3, 3, 4, 7]

lst1= [int(val) for val in input("Please enter your values of list1: ").split()]
print("="*60)
lst2= [int(val) for val in input("Please enter your values of list2: ").split()]
print("="*60)
print(f"""Original lists: {lst1}
                {lst2}""")
for val in lst2:
    if val in lst1:
        lst1.remove(val)
print(f"Difference between two said list including duplicate elements: {lst1}")