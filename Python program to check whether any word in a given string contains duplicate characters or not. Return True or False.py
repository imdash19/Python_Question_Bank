# Write a Python program to check whether any word in a given string contains duplicate characters or not. Return True or False.
# Sample Output:
# Original text:
# Filter out the factorials of the said list.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# Python Exercise.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# The wait is over.
# Check whether any word in the said sting contains duplicate characrters or not!
# True

text = input("Enter a string:\n")

words = text.split()

result = False

for word in words:
    cleaned = ''.join(char.lower() for char in word if char.isalpha())
    if len(cleaned) != len(set(cleaned)):
        result = True
        break

print("Check whether any word in the said string contains duplicate characters or not!")
print(result)