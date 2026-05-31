# Reads a complete matrix input where the first line specifies dimensions and subsequent lines contain the matrix elements row by row. The program constructs a proper 2D list representation.

rows = int(input())
columns = int(input())

matrix = []

for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
