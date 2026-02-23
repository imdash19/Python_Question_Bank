# Write a Python program to make combinations of 3 digits.

import itertools
def generate_combinations():
    digits = list(range(10))  # 0 to 9

    print("=" * 60)
    print("All possible 3-digit combinations:\n")

    count = 0
    for combo in itertools.combinations(digits, 3):
        print(combo)
        count += 1

    print("\n" + "=" * 60)
    print("Total combinations:", count)
generate_combinations()