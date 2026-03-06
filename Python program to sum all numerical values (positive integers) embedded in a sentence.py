# Write a Python program to sum all numerical values (positive integers) embedded in a sentence.
# Input: Sentences with positive integers are given over multiple lines. Each line is a character string containing one-byte alphanumeric characters, symbols, spaces, or an empty line. However, the input is 80 characters or less per line and the sum is 10,000 or less.
# Input some text and numeric values (to exit):
# Sum of the numeric values: 80
# None
# Input some text and numeric values (to exit):
# Sum of the numeric values: 17
# None
# Input some text and numeric values (to exit):
# Sum of the numeric values: 10
# None

while True:
    s = input("Input some text and numeric values (to exit): ")
    if s == "":
        break
    num = ""
    total = 0
    for i in s:
        if i.isdigit():
            num += i
        else:
            if num != "":
                total += int(num)
                num = ""
    if num != "":
        total += int(num)
    print("Sum of the numeric values:", total)