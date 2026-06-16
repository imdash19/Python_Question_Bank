# Reads a long string and truncates it to a specified maximum length with ellipsis (...) using .format() method. Useful for displaying previews or summaries of long text.

text = input()
max_length = int(input())

if len(text) > max_length:
    text = text[:max_length - 3] + "..."

print("{}".format(text))
