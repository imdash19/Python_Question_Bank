# Write a Python program to compute the sum of the first n prime numbers.
# Input: n (n <= 10000). Input 0 to exit the program.
# Input a number (n<=10000) to compute the sum:(0 to exit)
# 25
# Sum of first 25 prime numbers: 1060

while True:
    n = int(input("Input a number (n<=10000) to compute the sum:(0 to exit)\n"))
    if n == 0:
        break
    count = 0
    num = 2
    s = 0
    while count < n:
        prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                prime = False
                break
            i += 1
        if prime:
            s += num
            count += 1
        num += 1
    print("Sum of first", n, "prime numbers:", s)