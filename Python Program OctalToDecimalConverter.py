# Reads an octal number (string of digits 0-7) and converts it to its decimal (integer) equivalent. Validates that input contains only valid octal digits.

octal_num = input().strip()

if all(digit in "01234567" for digit in octal_num):
    print(int(octal_num, 8))
else:
    print("Invalid Octal Number")