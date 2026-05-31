# Reads multiple lines of text until a termination condition (like a specific sentinel or empty line). The program collects all lines into a list for text processing or analysis.

lines = []

while True:
    text = input()
    
    if text == "":
        break
    
    lines.append(text)

print(lines)
