# Write a Python program to convert a given string to Camelcase.
# Sample Output:
# javascript
# fooBar
# fooBar
# foo.Bar
# fooBar
# foobar
# fooBar

import re

s = input().strip()

words = re.split(r'[\s_\-\.]+', s)

if words:
    result = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
else:
    result = ""

print(result)