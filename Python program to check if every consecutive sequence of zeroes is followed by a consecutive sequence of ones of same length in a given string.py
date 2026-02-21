# Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string: True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string: False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string: True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string: False

def check_sequence(s):
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '0':
            zero_count = 0
            while i < n and s[i] == '0':
                zero_count += 1
                i += 1

            one_count = 0
            while i < n and s[i] == '1':
                one_count += 1
                i += 1

            if zero_count != one_count:
                return False
        else:
            i += 1

    return True

sequence = input("Original sequence: ")

result = check_sequence(sequence)

print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:",
      result)