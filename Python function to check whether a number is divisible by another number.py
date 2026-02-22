def check_number_divisible():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if b == 0:
        print("Division by zero is not allowed.")
        return

    if a % b == 0:
        print("Number is divisible by another number")
    else:
        print("Number is not divisible by another number")

check_number_divisible()