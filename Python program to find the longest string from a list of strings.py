# Write a Python program to find the longest string from a list of strings.
# The program should ask the user to enter a list of strings, separated by commas.
# Compare the length of each string to determine the longest.
# Use Python’s functools.reduce() function to compare strings successively.
# Finally, display the longest string.

strings = input("Enter strings separated by commas: ").split(",")

longest = max(strings, key=len)

print("Longest string:", longest.strip())
