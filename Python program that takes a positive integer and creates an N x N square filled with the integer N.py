# Write a Python program that takes a positive integer and creates an N x N square filled with the integer N. Display the N x N square.
# Sample Data:
# (2) -> [[2, 2], [2, 2]]
# (5) -> [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
# (-6) -> []

def create_square():
    n = int(input())

    if n <= 0:
        return []

    return [[n] * n for _ in range(n)]


print(create_square())