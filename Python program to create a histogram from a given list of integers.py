# Write a Python program to create a histogram from a given list of integers.

def create_histogram(numbers):
    for num in numbers:
        print('*' * num)

user_input = input("Enter integers separated by commas: ")
numbers = list(map(int, user_input.split(',')))

print('=' * 50)
create_histogram(numbers)