# Write a Python program to convert a given heterogeneous list of scalars into a string.
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False

lst = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]

print("Original list:")
print(lst)

result = ",".join(map(str, lst))

print("Convert the heterogeneous list of scalars into a string:")
print(result)