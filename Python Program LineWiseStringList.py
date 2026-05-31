# Reads multiple strings where each string appears on a new line. The program gathers these strings into a list, preserving their order and original formatting.

n = int(input())

strings = []

for _ in range(n):
    strings.append(input())

print(strings)
