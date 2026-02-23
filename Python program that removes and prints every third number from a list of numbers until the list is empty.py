# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

def remove_every_third():
    nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("=" * 60)
    index = 0
    while nums:
        index = (index + 2) % len(nums)
        removed = nums.pop(index)
        print("Removed:", removed)
        print("Remaining list:", nums)
        print("-" * 40)

remove_every_third()