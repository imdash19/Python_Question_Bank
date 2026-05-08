# Write a Python program to replace all duplicate occurrences of characters in a string with a symbol (e.g., *). 
# The program should accept a string input. The first occurrence remains unchanged. 
# Case should be preserved. Output must show transformed string.

s = input()
d = []

for v in s:
    if v not in d:
        print(v, end= '')
        d.append(v)
    else:
        print('*', end= '')
