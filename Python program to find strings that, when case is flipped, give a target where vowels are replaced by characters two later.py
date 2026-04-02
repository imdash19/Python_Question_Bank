# Write a Python program to find strings that, when case is flipped, give a target where vowels are replaced by characters two later.
# Input: Python
# Output:
# pYTHQN
# Input: aeiou
# Output:
# CGKQW
# Input: Hello, world!
# Output:
# hGLLQ, WQRLD!
# Input: AEIOU
# Output:
# cgkqw

s = input()

vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch.islower():
        ch = ch.upper()
    elif ch.isupper():
        ch = ch.lower()

    if ch in vowels:
        ch = chr(ord(ch) + 2)

    result += ch

print(result)