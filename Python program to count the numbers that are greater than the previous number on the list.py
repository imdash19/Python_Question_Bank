# A Python list contains some positive integers. Write a Python program to count the numbers that are greater than the previous number on the list.
# Sample Data:
# ([1, 4, 7, 9, 11, 5]) -> 4
# ([1, 3, 3, 2, 2]) -> 1
# ([4, 3, 2, 1]) -> 0

def count_greater():
    lst = list(map(int, input().split()))

    count = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            count += 1

    return count


print(count_greater())