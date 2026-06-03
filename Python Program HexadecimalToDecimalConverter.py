# Reads a hexadecimal number as input (string containing 0-9 and A-F) and converts it to its decimal (integer) equivalent. Validates the hex format before conversion.

hex_num = input().strip()

try:
    decimal = int(hex_num, 16)
    print(decimal)
except ValueError:
    print("Invalid Hexadecimal Number")