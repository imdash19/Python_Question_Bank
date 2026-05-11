# Write a Python program to count the number of elements that are the same at the same position in three lists.
# The program should accept three space-separated lists from the user.
# Compare elements that are at the same index in all three lists.
# Use Python’s built-in zip() function for parallel iteration.
# Use list comprehension to count matching elements.
# Display the total count clearly.

def count_same_positions(list1, list2, list3):
    return sum(1 for a, b, c in zip(list1, list2, list3) if a == b == c)

if __name__ == "__main__":
    list1 = input().split(":")[-1].strip().split()
    list2 = input().split(":")[-1].strip().split()
    list3 = input().split(":")[-1].strip().split()

    result = count_same_positions(list1, list2, list3)

    print("Number of same elements at the same position:", result)
