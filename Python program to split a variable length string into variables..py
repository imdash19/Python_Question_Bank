# Write a Python program to split a variable length string into variables.

def split_string():
    text = input("Enter words separated by space: ")
    print("=" * 50)
    words = text.split()
    for i, word in enumerate(words, start=1):
        print(f"Variable {i} =", word)
split_string()