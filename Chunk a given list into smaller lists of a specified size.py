# 	Write a Python program to chunk a given list into smaller lists of a specified size.
# Sample Output: [[1, 2, 3], [4, 5, 6], [7, 8]]

lst = list(map(int, input("Enter list elements separated by space: ").split()))
size = int(input("Enter chunk size: "))

chunks = [lst[i:i + size] for i in range(0, len(lst), size)]
print(chunks)