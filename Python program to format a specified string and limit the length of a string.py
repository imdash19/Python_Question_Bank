# Write a Python program to format a specified string and limit the length of the string.

def format_and_limit_string():
    try:
        text = input("Enter a string: ")
        limit = int(input("Enter maximum length: "))
        limited_text = text[:limit]
        formatted_text = f"{limited_text:^30}"

        print("\nOriginal String:", text)
        print("Limited String:", limited_text)
        print("Formatted String (center aligned, width 30):")
        print(formatted_text)

    except ValueError:
        print("Error: Please enter a valid number for length.")

format_and_limit_string()