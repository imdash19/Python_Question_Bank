# Write a Python program to get the ASCII value of a character.

def get_ascii_value():
    ch = input("Enter a character: ")

    if len(ch) != 1:
        print("Please enter only a single character.")
    else:
        print(f"ASCII value of '{ch}' is {ord(ch)}")

get_ascii_value()