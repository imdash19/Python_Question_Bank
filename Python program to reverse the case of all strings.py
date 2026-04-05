# Write a Python program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.
# Original list:
# ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']
# Original list:
# ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']
# Original list:
# ['Hello', '!@#', '!@#$', '123#@!']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['hELLO', '#@!', '$#@!', '!@#321']

lst = eval(input())

res = []

for s in lst:
    if any(ch.isalpha() for ch in s):
        res.append(s.swapcase())
    else:
        res.append(s[::-1])

print(res)