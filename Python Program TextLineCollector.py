# Reads multiple lines of text input until an empty line is encountered. The program collects all non-empty lines into a list, useful for reading variable-length textual input.

lines = []

while True:
    text = input()

    if text == "":
        break

    lines.append(text)

print(lines)
