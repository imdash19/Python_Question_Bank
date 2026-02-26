# Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a line without spaces between them.

given_number = input("Enter the number formed by sequential powers of 2: ")

sequence = ""
n = 1

while len(sequence) < len(given_number):
    power_value = str(2 ** n)
    sequence += power_value

    if sequence == given_number:
        print("Value of n is:", n)
        break

    n += 1
else:
    print("The given number is NOT formed by sequential powers of 2.")