# "Secure Assets Private Ltd", a small company that deals with lockers has recently started manufacturing digital locks which can be locked and unlocked using PINs (passwords). You have been asked to work on the module that is expected to generate PINs using three input numbers. The three given input numbers will always consist of three digits each i.e. each of them will be in the range >=100 and <=999.
# Below are the rules for generating the PIN.
# i.	The PIN should made up of 4 digits.
# ii.	The unit (ones) position of the PIN should be the least of the units position of the three numbers.
# iii.	The tens position of the PIN should be the least of the tens position of the three input numbers.
# iv.	The hundreds position of the PIN should be least of the hundreds position of the three numbers.
# v.	The thousands position of the PIN should be the max of all digits in the three input numbers.
# Input Format
# Three numbers
# Constraints
# all the numbers must be in the range of >= 100 and <= 999
# Output Format
# PIN value
# Sample Input 0
# 123
# 582
# 175
# Sample Output 0
# 8122

def generate_pin():
    a = input().strip()
    b = input().strip()
    c = input().strip()

    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        return

    a, b, c = int(a), int(b), int(c)

    if not (100 <= a <= 999 and 100 <= b <= 999 and 100 <= c <= 999):
        return

    u = min(a % 10, b % 10, c % 10)
    t = min((a // 10) % 10, (b // 10) % 10, (c // 10) % 10)
    h = min(a // 100, b // 100, c // 100)

    digits = list(map(int, str(a) + str(b) + str(c)))
    th = max(digits)

    pin = th * 1000 + h * 100 + t * 10 + u

    return pin

print(generate_pin())