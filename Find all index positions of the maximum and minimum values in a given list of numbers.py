# Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
# Original list: [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# Index positions of the maximum value of the said list: 7
# Index positions of the minimum value of the said list: 3

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("="*60)
x= max(lst)
n= min(lst)
print(f"""Original list: {lst}
Index positions of the maximum value of the said list: {lst.index(x)}
Index positions of the minimum value of the said list: {lst.index(n)}""")