# Create class Number with static method is_even that checks if input number is even or odd

class Number:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

n = int(input())
Number.is_even(n)
