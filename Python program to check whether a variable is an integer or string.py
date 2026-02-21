# Write a Python program to check whether a variable is an integer or string.

value = input("Enter a value: ")
try:
    int_value = int(value)
    if '.' not in value:
        print("The variable is of type: Integer")
    else:
        print("The variable is of type: String")

except ValueError:
    print("The variable is of type: String")