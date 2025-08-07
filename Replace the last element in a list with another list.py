# Write a PYTHON program to replace the last element in a list with another list.
# 	Sample data: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

lst1 = [val for val in input("Please input your for list1 values with space: ").split()]
print("-"*70)

lst2 = [val for val in input("Please input your for list2 values with space: ").split()]
print("-"*70)

if(len(lst1) == 0 or len(lst2) == 0):
    print("Please enter some values in the list")
    print("-" * 70)

else:
    lst1.pop()
    lst1.extend(lst2)
    print(lst1)
    print("-" * 70)

print("program executed successfully")
