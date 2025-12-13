#  Write a Python program to convert a given decimal number to binary list.
# Original Number: 8
# Decimal number (8) to binary list: [1, 0, 0, 0]
# Original Number: 45
# Decimal number (45) to binary list: [1, 0, 1, 1, 0, 1]
# Original Number: 100
# Decimal number (100) to binary list: [1, 1, 0, 0, 1, 0, 0]

def decimal_to_binary(num):
    olst = []
    rem= num % 2
    olst.append(rem)
    num= num // 2
    if num == 0:
        return olst
    else:
        olst.extend(decimal_to_binary(num))
        return olst

try:
    num= int(input('Please enter number: '))
    print('='*60)

except ValueError:
    print('Please enter number...')

except Exception:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original Number: {num}
# Decimal number ({num}) to binary list: {decimal_to_binary(num)}''')