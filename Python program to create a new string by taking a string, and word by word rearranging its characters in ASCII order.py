# Write a Python program to create a new string by taking a string, and word by word rearranging its characters in ASCII order.
# Input: Ascii character table
# Output: Aciis aaccehrrt abelt
# Input: maltos won
# Output: almost now

s= input('Please enter a string: ').split()
lst= []

for v in s:
    ilst= []
    for sv in v:
        ilst.append(ord(sv))
    ilst.sort()
    lst.append(ilst)

for v in lst:
    for sv in v:
        print(chr(sv), end="")
    print(end=' ')