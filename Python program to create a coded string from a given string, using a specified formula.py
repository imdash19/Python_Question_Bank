# Write a Python program to create a coded string from a given string, using a specified formula.
# Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with '8'
# Original string: PHP
# Coded string: 969
# Original string: JAVASCRIPT
# Coded string: J8V81CRI90

def replace_values_from_string():
    s= input()
    s= s.replace('P', '9')
    s= s.replace('T', '0')
    s= s.replace('S', '1')
    s= s.replace('H', '6')
    s= s.replace('A', '8')

    print(s)
    return

replace_values_from_string()