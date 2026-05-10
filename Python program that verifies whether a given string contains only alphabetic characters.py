# Create a program that verifies whether a given string contains only alphabetic characters. The program should accept a string from the user and check if every single character in that string is a letter from A to Z (either uppercase or lowercase). No numbers, spaces, punctuation marks, or special symbols should be present in the string for it to be considered valid.You will implement this validation using Python's regular expression module with the re.fullmatch() function. The fullmatch() function is crucial here because it ensures that the entire string from start to finish matches our alphabet pattern, leaving no room for any non-alphabetic characters to sneak in.Input Format:

# A single line containing a string to be validated
# Output Format:

# Print "Valid string" if the string contains only alphabets (both uppercase and lowercase allowed)
# Print "Invalid string" if the string contains any non-alphabetic characters

s = input()

if s.isalpha():
    print("True")
else:
    print("False")
