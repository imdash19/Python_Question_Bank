# Write a Python program to reverse a given string in lower case.
# Original string: PHP
# Reverse the said string in lower case: php
# Original string: JavaScript
# Reverse the said string in lower case: tpircsavaj
# Original string: PHPP
# Reverse the said string in lower case: pphp

def reverse_string_in_lower_case():
    s= input()
    s= s.lower()
    return s[::-1]

print(reverse_string_in_lower_case())