# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

def get_numbers_divisible_by_fifteen():
    user_input = input("Enter numbers separated by space: ").strip()

    if not user_input:
        print("Invalid input!")
        return

    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Please enter only integers.")
        return

    divisible_by_15 = list(filter(lambda x: x % 15 == 0, numbers))

    print("=" * 50)
    print("Numbers divisible by 15:", divisible_by_15)
    print("=" * 50)

if __name__ == "__main__":
    get_numbers_divisible_by_fifteen()