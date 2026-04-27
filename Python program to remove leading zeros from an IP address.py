# Write a Python program to remove leading zeros from an IP address.

ip = input().split('.')
res = []

for part in ip:
    num = str(int(part))
    res.append(num)

print(".".join(res))