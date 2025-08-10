# Write a PYTHON program to insert an element at a specified position into a given list.
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After inserting an element at kth position in the said list:
# 	[1, 1, 12, 2, 3, 4, 4, 5, 1]

try:
    lst = [ele for ele in input("Please enter your elements separated with space: ").split()]
    print("-"*70)
    i = int(input("Please the kth position to insert element: "))
    print("-" * 70)
    ele = input("Please enter the element: ")
    print("-" * 70)
    lst.insert(i-1, ele)

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)

except IndexError as i:
    print("-" * 70)
    print("Please enter a valid index: ", i)
    print("-" * 70)

except Exception as e:
    print("Something went wrong! Please check again.", e)

else:
    print(lst)
    print("-" * 70)

finally:
    print("Program executed successfully")