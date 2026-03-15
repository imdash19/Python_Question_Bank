# Write a Python program to create a string with no duplicate consecutive letters from a given string.
# Sample Input:
# ("PPYYYTTHON")
# ("PPyyythonnn")
# ("Java")
# ("PPPHHHPPP")
# Sample Output:
# PYTHON
# Python
# Java
# PHP

s = input()

result = s[0]

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        result += s[i]

print(result)