# Write a Python program to sort numbers based on strings.
# Input: six one four one two three
# Output:
# one two three four six
# Input: six one four three two nine eight
# Output:
# one two three four six eight nine
# Input: nine eight seven six five four three two one
# Output:
# one two three four five six seven eight nine

order = {
    "zero": 0, "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9
}

words = input().split()
words.sort(key=lambda x: order[x])
print(" ".join(words))