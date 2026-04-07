# Write a Python program to shift the decimal digits n places to the left, wrapping the extra digits around. If the shift > the number of digits in n, reverse the string.
# Input: n = 12345 and shift = 1
# Output: Result = 23451
# Input: n = 12345 and shift = 2
# Output: Result = 34512
# Input: n = 12345 and shift = 3
# Output: Result = 45123
# Input: n = 12345 and shift = 5
# Output: Result = 12345
# Input: n = 12345 and shift = 6
# Output: Result = 54321

def left_shift(num, shift):
    s = str(num)
    l = len(s)
    if shift > l:
        return int(s[::-1])
    shift = shift % l
    return int(s[shift:] + s[:shift])

n = int(input())
shift = int(input())
print(left_shift(n, shift))