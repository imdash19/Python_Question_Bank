# 	Write a Python program to initialize and fills a list with the specified value.
# Sample Output: [0, 0, 0, 0, 0, 0, 0]
#     [3, 3, 3, 3, 3, 3, 3, 3]
#     [-2, -2, -2, -2, -2]
#     [3.2, 3.2, 3.2, 3.2, 3.2]

size = int(input("Enter the size of the list: "))
value = input("Enter the value to fill the list with: ")

try:
    if "." in value:
        value = float(value)
    else:
        value = int(value)
except ValueError:
    pass

result = [value] * size
print(result)