# Write a Python program to split a multi-line string into a list of lines.
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']


lines = []
print("Enter multiline string (type END to stop):")
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

result = []
for l in lines:
    result.append(l)

result.append('')

print("Split the said multiline string into a list of lines:")
print(result)