# When character is consecutive in a string, it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.
# Write a Python program to restore the original string by entering the compressed string with this rule. However, the # character does not appear in the restored character string.
# Input:
# The restored character string for each character on one line.
# Original text: XY#6Z1#4023
# XYZZZZZZ1000023
# Original text: #39+1=1#30
# 999+1=1000

s = input("Original text: ")
i = 0
res = ""

while i < len(s):
    if s[i] == "#":
        i += 1
        num = ""
        while s[i].isdigit():
            num += s[i]
            i += 1
        res += s[i] * int(num)
        i += 1
    else:
        res += s[i]
        i += 1

print(res)