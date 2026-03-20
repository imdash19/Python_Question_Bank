# Write a Python program to check if a given string contains two similar consecutive letters.
# Original string: PHP
# Check for consecutive similar letters! False
# Original string: PHHP
# Check for consecutive similar letters! True
# Original string: PHPP
# Check for consecutive similar letters! True

def check_if_string_contains_only_lowercase_characters():
    s= input()
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            print(True)
            return
    else:
        print(False)
        return

check_if_string_contains_only_lowercase_characters()