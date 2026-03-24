# Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of the same length in a given string. Return True/False.
# Original sequence: 001011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 0011101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False

def check_sequence(s):
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '0':
            z = 0
            while i < n and s[i] == '0':
                z += 1
                i += 1

            o = 0
            while i < n and s[i] == '1':
                o += 1
                i += 1

            if z != o:
                return False
        else:
            i += 1

    return True


print(check_sequence(input()))