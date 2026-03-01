# Write a Python program to count the number of carry operations for each addition problem.
# According to Wikipedia " In elementary arithmetic, a carry is a digit that is transferred from one column of digits to another column of more significant digits. It is part of the standard algorithm to add numbers together by starting with the rightmost digits and working to the left. For example, when 6 and 7 are added to make 13, the "3" is written to the same column and the "1" is carried to the left".

def count_carry(a, b):
    carry = 0
    count = 0
    while a > 0 or b > 0:
        if (a % 10 + b % 10 + carry) >= 10:
            carry = 1
            count += 1
        else:
            carry = 0
        a //= 10
        b //= 10
    return count

while True:
    x, y = input().split()
    if x == '0' and y == '0':
        break
    x = int(x)
    y = int(y)
    result = count_carry(x, y)
    if result == 0:
        print("No carry operation.")
    elif result == 1:
        print("1 carry operation.")
    else:
        print(result, "carry operations.")