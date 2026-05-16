# Write a program to count the number of uppercase letters in a string using recursion.
# The program should take a string input from the user.
# Each recursive call examines the first character.
# If uppercase, increment count.
# Recursion stops when string is empty. Output is integer.

s= input()
cnt= 0
for v in s:
    if v.isupper():
        cnt+= 1

print(cnt)
