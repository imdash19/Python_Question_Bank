# Write a Python program to find the XOR of two given strings interpreted as binary numbers.
# Input:
# ['0001', '1011']
# Output:
# 0b1010
# Input:
# ['100011101100001', '100101100101110']
# Output:
# 0b110001001111

s1 = input().strip()
s2 = input().strip()

result = int(s1, 2) ^ int(s2, 2)

print(bin(result))