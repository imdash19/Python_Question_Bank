# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

import itertools
def generate_strings():
    letters = ['a', 'e', 'i', 'o', 'I']
    print("=" * 60)
    print("All possible strings using each character exactly once:\n")
    count = 0
    for perm in itertools.permutations(letters):
        print(''.join(perm))
        count += 1

    print("\n" + "=" * 60)
    print("Total strings generated:", count)

generate_strings()