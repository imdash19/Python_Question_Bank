# Write a Python program to test if a variable is a list, tuple, or set.

# You can change this value to test
value = eval(input("Enter a Python collection (e.g., [1,2], (1,2), {1,2}): "))

if isinstance(value, list):
    print("The variable is a List.")
elif isinstance(value, tuple):
    print("The variable is a Tuple.")
elif isinstance(value, set):
    print("The variable is a Set.")
else:
    print("The variable is NOT a List, Tuple, or Set.")