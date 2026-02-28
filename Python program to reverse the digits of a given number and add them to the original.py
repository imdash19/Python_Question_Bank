# Write a Python program to reverse the digits of a given number and add them to the original. Repeat this procedure if the sum is not a palindrome.
# Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or race car.

def reverse_add_palindrome():
    n = int(input("Enter a number: "))

    while True:
        rev = int(str(n)[::-1])
        total = n + rev
        print(n, "+", rev, "=", total)

        if str(total) == str(total)[::-1]:
            print("Palindrome obtained:", total)
            break

        n = total

reverse_add_palindrome()