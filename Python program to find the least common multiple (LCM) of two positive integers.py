# Write a Python program to find the least common multiple (LCM) of two positive integers.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

a= int(input('Please enter a positive integer: '))
b= int(input('Please enter a positive integer: '))

print(f'''LCM of {a} and {b} is {find_lcm(a, b)}''')