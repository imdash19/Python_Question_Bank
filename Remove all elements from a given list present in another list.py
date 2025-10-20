# Write a Python program to remove all elements from a given list present in another list.
# Original lists: list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2': [1, 3, 5, 7, 9, 10]

lst1= [int(val) for val in input("Please enter your values for list1 separated with space: ").split()]
print("-"*60)
lst2= [int(val) for val in input("Please enter your values for list2 separated with space: ").split()]
print("-"*60)

print(f"""Original lists: 
            list1: {lst1}
            list2: {lst2}""")

for val in lst2:
    if val in lst1:
        lst1.remove(val)

print("Remove all elements from 'list1' present in 'list2': ", lst1)