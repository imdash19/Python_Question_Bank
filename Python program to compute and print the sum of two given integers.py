# Write a Python program to compute and print the sum of two given integers (greater or equal to zero). In the event that the given integers or the sum exceeds 80 digits, print "overflow".
# Input first integer: 25
# Input second integer: 22
# Sum of the two integers: 47

def cal_sum():
    a = input()
    b = input()

    if not (a.isdigit() and b.isdigit()):
        print("overflow")
        return

    if len(a) > 80 or len(b) > 80:
        print("overflow")
        return

    s = str(int(a) + int(b))

    if len(s) > 80:
        print("overflow")
        return

    print("Sum of the two integers:", s)

cal_sum()