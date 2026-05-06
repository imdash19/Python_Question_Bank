# Write a Python program that takes a string and replaces all the characters with their respective numbers.
# Sample Data:
# ("Python") -> "16 25 20 8 15 14"
# ("Java") -> "10 1 22 1"
# ("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"

text = input().lower()

result = []

for ch in text:
    if ch.isalpha():
        result.append(str(ord(ch) - 96))

print(" ".join(result))