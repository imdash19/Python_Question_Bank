# A Python list contains three positive integers. Write a Python program to check whether the sum of the digits in each number is equal or not. Return true otherwise false.
# Sample Data:
# ([13, 4, 22]) -> True
# ([-13, 4, 22]) -> False
# ([45, 63, 90]) -> True

def digit_sum(n):
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s


def check_sum_of_digits():
    lst = list(map(int, input().split()))

    if any(x < 0 for x in lst) or len(lst) != 3:
        return False

    s1 = digit_sum(lst[0])
    s2 = digit_sum(lst[1])
    s3 = digit_sum(lst[2])

    return s1 == s2 == s3


obj = check_sum_of_digits()
print(True) if obj else print(False)