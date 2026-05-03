# Write a Python program to convert a given string to Snake case.
# Sample Output:
# java_script
# foo_bar
# foo_bar
# foo.bar
# foo_bar
# foo_bar
# foo_bar

import re

s = input().strip()

s = re.sub(r'([a-z])([A-Z])', r'\1_\2', s)

words = re.split(r'[\s\-_]+', s)

result = "_".join(word.lower() for word in words if word)

print(result)