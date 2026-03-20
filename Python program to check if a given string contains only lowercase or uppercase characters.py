# Write a Python program to check if a given string contains only lowercase or uppercase characters.
# Original string: PHP
# Coded string: True
# Original string: javascript
# Coded string: True
# Original string: JavaScript
# Coded string: False

def check_if_string_contains_only_lowercase_or_uppercase_characters():
    s= input()
    print(True) if s.islower() or s.isupper() else print(False)
    return

check_if_string_contains_only_lowercase_or_uppercase_characters()