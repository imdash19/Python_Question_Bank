# Reads an integer and formats it with explicit sign (+ or -) always shown using .format() method. Useful for mathematical displays where sign visibility is important.

number = int(input())

print("{:+d}".format(number))
