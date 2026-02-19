# Write a Python program to input two integers on a single line.

def input_two_integers():
    try:
        a, b = map(int, input("Enter two integers separated by space: ").split())
        print("\nFirst Integer:", a)
        print("Second Integer:", b)

    except ValueError:
        print("Error: Please enter exactly two valid integers.")

input_two_integers()