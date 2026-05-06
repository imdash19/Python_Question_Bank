# Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation.
# Sample Data:
# ( "234242342341", "2432342342") -> "236674684683"
# ( "", "2432342342") -> False ( "1000", "0") -> "1000"
# ( "1000", "10") -> "1010"

a = input()
b = input()

if a == "" or b == "":
    print(False)
else:
    result = str(int(a) + int(b))
    print(result)