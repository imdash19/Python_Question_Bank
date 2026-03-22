# Write a Python program to find all the factors of a given natural number.
# Factors:
# The factors of a number are the numbers that divide into it exactly. The number 12 has six factors:
# 1, 2, 3, 4, 6 and 12 If 12 is divided by any of the six factors then the answer will be a whole number. For example:
# 12 / 3 = 4
# Original Number: 1
# Factors of the said number: {1}
# Original Number: 12
# Factors of the said number: {1, 2, 3, 4, 6, 12}
# Original Number: 100
# Factors of the said number: {1, 2, 4, 100, 5, 10, 50, 20, 25}

n = int(input())
factors = []
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)
print("Factors of the said number:", set(factors))