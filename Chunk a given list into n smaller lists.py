# Write a Python program to chunk a given list into n smaller lists.
# Sample Output: [[1, 2], [3, 4], [5, 6], [7]]

lst = list(map(int, input("Enter list elements: ").split()))
n = int(input("Enter number of chunks: "))

k = len(lst) // n
r = len(lst) % n

chunks = []
start = 0

for i in range(n):
    end = start + k + (1 if i < r else 0)
    chunks.append(lst[start:end])
    start = end

print(chunks)