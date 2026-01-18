# 	Write a Python program to initialize a list containing the numbers in the specified range where start and end are inclusive and the ratio between two terms is step. Returns an error if step equals 1.
# Sample Output: [1, 2, 4, 8, 16, 32, 64, 128, 256]
#     [3, 6, 12, 24, 48, 96, 192]
#     [1, 4, 16, 64, 256]

start = int(input("Enter start value: "))
end = int(input("Enter end value: "))
step = int(input("Enter step (ratio): "))

if step == 1:
    raise ValueError("Step cannot be 1")

result = []
value = start

while value <= end:
    result.append(value)
    value *= step

print(result)