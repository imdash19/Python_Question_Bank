# Write a PYTHON program to remove the Kth element from a given list, print the new list.
# Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After removing an element at the kth position of the said list:
# 	[1, 1, 3, 4, 4, 5, 1]

try:
    lst = [ele for ele in input("Please enter your elements separated with space: ").split()]
    print("-"*70)
    n = int(input("Please enter the Kth position: "))
    print("-" * 70)
    lst.pop(n-1)

except ValueError as v:
    print("-" * 70)
    print("Please enter a number: ", v)
    print("-" * 70)
    
except IndexError as i:
    print("-" * 70)
    print("Please enter a valid position: ", i)
    print("-" * 70)

except Exception as e:
    print("-" * 70)
    print("Something wnt wrong! Please check again.", e)
    print("-" * 70)

else:
    print("After removing an element at the kth position of the said list: ",lst)
    print("-" * 70)

finally:
    print("Program executed successfully")