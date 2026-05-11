# Write a Python program to interleave multiple lists of the same length.
# The program should accept multiple space-separated lists from the user.
# All lists will be of the same length.
# Use Python’s built-in zip() function to combine elements position-wise.
# Use list comprehension to interleave the elements alternately.
# Display the interleaved list clearly.

def interleave_lists(lists):
    return [item for group in zip(*lists) for item in group]

if __name__ == "__main__":
    n = int(input().split(":")[-1].strip())

    lists = []

    for _ in range(n):
        elements = input().split(":")[-1].strip().split()
        lists.append(elements)

    result = interleave_lists(lists)

    print("Interleaved list:", result)
