# Write a Python program to define a string containing special characters in various forms.

def special_characters_demo():
    print("=" * 60)
    print("Demonstration of Special Characters in Various Forms")
    print("=" * 60)

    print("\n1. Escape Sequences:")
    escape_string = "Hello\nWorld!\tWelcome to \"Python\" programming.\nBackslash example: \\"
    print(escape_string)

    print("\n2. Raw String:")
    raw_string = r"C:\Users\NewFolder\test.py"
    print(raw_string)

    print("\n3. Triple-Quoted String:")
    triple_string = """This is a multi-line string.
It can contain "quotes" and 'single quotes'.
Special characters like \n are written as text here."""
    print(triple_string)

    print("\n4. Unicode Characters:")
    unicode_string = "Heart: \u2764  Smiley: \U0001F600"
    print(unicode_string)

    print("\n5. User Input with Special Characters:")
    user_string = input("Enter a string with special characters: ")
    print("You entered:", user_string)

    print("\n" + "=" * 60)
    print("End of demonstration")
    print("=" * 60)

special_characters_demo()