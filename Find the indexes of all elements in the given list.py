# Write a Python program to find the indexes of all elements in the given list that satisfy the provided testing function.
# Sample Output: [0, 2]

def test_func(x):
    return x > 10

nums = [12, 5, 15, 8]

indexes = [i for i, v in enumerate(nums) if test_func(v)]

print(indexes)