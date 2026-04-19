# Write a Python program to create a Caesar encryption.
# Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

text = input()
shift = int(input())

result = ""

for ch in text:
    if ch.isalpha():
        if ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    else:
        result += ch

print(result)