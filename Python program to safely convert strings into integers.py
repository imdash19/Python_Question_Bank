# Write a program to safely convert strings into integers.
# The program should accept a space-separated list of values.
# If conversion is possible, convert to integer.
# If conversion fails, replace it with 0.
# The program should use map() with a helper function.
# The output should be a list of integers.

def safe_convert(value):
    try:
        return int(value)
    except:
        return 0

values = input().split()

result = list(map(safe_convert, values))

print(result)
