# Reads an email address as input and validates it against standard email format rules. The program checks for proper structure including "@" symbol and domain format.

import re

email = input()

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
