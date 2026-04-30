# Write a Python program to wrap a given string into a paragraph with a given width.
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.

def wrap_text(s, width):
    words = s.split()
    line = ""
    result = ""

    for word in words:
        if len(line) == 0:
            line = word
        elif len(line) + 1 + len(word) <= width:
            line += " " + word
        else:
            result += line + "\n"
            line = word

    result += line
    return result

s = input("Input a string: ")
width = int(input("Input the width of the paragraph: "))

print("Result:")
print(wrap_text(s, width))