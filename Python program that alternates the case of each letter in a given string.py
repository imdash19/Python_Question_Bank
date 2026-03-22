# Write a Python program that alternates the case of each letter in a given string, with the first letter in the string being uppercase.
# Original string: Python Exercises
# After alternating the case of each letter of the said string: PyThOn ExErCiSeS
# Original string: C# is used to develop web apps, desktop apps, mobile apps, games and much more.
# After alternating the case of each letter of the said string: C# iS uSeD tO dEvElOp WeB aPpS, dEsKtOp ApPs, MoBiLe ApPs, GaMeS aNd MuCh MoRe.

s = input()
result = ""
upper = True
for ch in s:
    if ch.isalpha():
        if upper:
            result += ch.upper()
        else:
            result += ch.lower()
        upper = not upper
    else:
        result += ch
print(result)