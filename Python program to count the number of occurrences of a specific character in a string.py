# Write a Python program to count the number of occurrences of a specific character in a string.

def count_specific_character():
    string = input("Enter your string: ")
    print("=" * 60)

    ch = input("Enter the specific character you want to count: ")
    print("=" * 60)

    if len(ch) != 1 or len(string) < 1:
        print("Invalid input!")
    else:
        count = 0
        for c in string:
            if c == ch:
                count += 1

        print(f"The number of occurrences of '{ch}' in '{string}' is {count}")

count_specific_character()