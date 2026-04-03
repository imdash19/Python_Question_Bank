# Write a Python program to find which characters of a hexadecimal number correspond to prime numbers.
# Input: 123ABCD
# Output:
# [False, True, True, False, True, False, True]
# Input: 123456
# Output:
# [False, True, True, False, True, False]
# Input: FACE
# Output:
# [False, False, False, False]

hex_str = input().upper()

prime_digits = {2, 3, 5, 7, 11, 13}

result = []

for ch in hex_str:
    value = int(ch, 16)
    if value in prime_digits:
        result.append(True)
    else:
        result.append(False)

print(result)