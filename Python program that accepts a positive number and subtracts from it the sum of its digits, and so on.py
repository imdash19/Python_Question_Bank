# Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on. Continue this operation until the number is positive.

def subtract():
    num = int(input("Enter a positive integer: "))
    print('=' * 60)

    if num <= 0:
        print("Please enter a positive integer.")
        return

    step = 1

    while num > 0:
        digit_sum = 0
        temp = num

        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

        print(f"Step {step}: {num} - {digit_sum} = {num - digit_sum}")
        num = num - digit_sum
        step += 1

    print('=' * 60)
    print("Process stopped. Final number:", num)

subtract()