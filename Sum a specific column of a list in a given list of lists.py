# Write a Python program to sum a specific column of a list in a given list of lists.
# Original list of lists: [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Sum: 1st column of the said list of lists: 12
# Sum: 2nd column of the said list of lists: 15
# Sum: 4th column of the said list of lists: 9

import numpy as np
n= int(input("Please enter how many inner list you want: "))
lst= []
for i in range(n):
    print("="*60)
    print(f"Inside {i+1} inner list")
    print("="*60)
    ilst= [int(val) for val in input("Please enter your values separated with space: ").split()]
    lst.append(ilst)

print(f"Original list: {lst}")
alst= np.array(lst)
print(f"""Sum: 1st column of the said list of lists: {np.sum(alst[:, 0])}
Sum: 2nd column of the said list of lists: {np.sum(alst[:, 1])}
Sum: 4th column of the said list of lists: {np.sum(alst[:, 3])}""")