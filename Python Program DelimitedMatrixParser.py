# Reads matrix data where rows are separated by one delimiter (e.g., semicolon) and elements within rows by another (e.g., space). Creates a 2D list from this structured input.

matrix_input = input()

matrix = [
    list(map(int, row.split()))
    for row in matrix_input.split(";")
]

print(matrix)