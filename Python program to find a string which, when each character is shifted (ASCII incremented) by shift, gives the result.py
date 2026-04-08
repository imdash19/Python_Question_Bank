# Write a Python program to find a string which, when each character is shifted (ASCII incremented) by shift, gives the result.
# Input: Ascii character table
# Shift = 1
# Output: @rbhh¬bg`q`bsdq¬s`akd
# Input: Ascii character table
# Shift = -1
# Output: Btdjj!dibsbdufs!ubcmf

s= list(input('Please enter your string: '))
sv= int(input('Please enter your shift value: '))
for v in s:
    print(chr(ord(v)-sv), end= '')