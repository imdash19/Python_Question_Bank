# Program to count the number of each character in a text file

def count_characters():
    filename = input("Enter the file name (with extension): ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        print("\n" + "="*60)
        print("File Content:\n")
        print(content)
        print("="*60)

        char_count = {}

        for ch in content:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        print("\nCharacter Frequency:\n")

        for ch, count in char_count.items():
            if ch == " ":
                print(f"Space : {count}")
            elif ch == "\n":
                print(f"Newline : {count}")
            elif ch == "\t":
                print(f"Tab : {count}")
            else:
                print(f"{ch} : {count}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except Exception as e:
        print("An error occurred:", e)

count_characters()