# Write a Python program to count the number of matching characters at the same position in two strings.
# The program should accept two strings of same or different length. 
# Compare character by character. 
# Output should display the count. Case should be ignored.

s1, s2= input(), input()
cnt= 0

for a, b in zip(s1, s2):
    if a == b:
        cnt+= 1

print(cnt)
