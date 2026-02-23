# Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers.

def find_three_sum():
    nums = [int(x) for x in input("Enter integers separated by space: ").split()]
    print("=" * 60)

    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    if result:
        print("Unique triplets whose sum is zero:")
        for triplet in result:
            print(triplet)
    else:
        print("No triplets found.")

find_three_sum()