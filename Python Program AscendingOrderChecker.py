# Reads a list of integers and checks whether they are already sorted in ascending order. The program validates the sort order without modifying the list.

numbers = list(map(int, input().split()))

if numbers == sorted(numbers):
    print("Sorted")
else:
    print("Not Sorted")