# Write a Python program to find the index of the first element in the given list that satisfies the provided testing function.
# Sample Output: 0

def test_func(x):
    return x > 10

nums = [12, 5, 8, 20]

index = next((i for i, v in enumerate(nums) if test_func(v)), -1)

print(index)