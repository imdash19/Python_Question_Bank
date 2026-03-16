# Write a Python program to test whether a given integer is a Pandigital number or not.
# From Wikipedia,
# In mathematics, a pandigital number is an integer that in a given base has among its significant digits each digit used in the base at least once.
# For example,
# 1223334444555556666667777777888888889999999990 is a pandigital number in base 10.
# The first few pandigital base 10 numbers are given by:
# 1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987, 1023457689
#
# Sample Output:
# Original number: 1023456897 Check the said number is Pandigital number or not? True Original number: 1023456798 Check the said number is Pandigital number or not? True Original number: 1023457689 Check the said number is Pandigital number or not? True Original number: 1023456789 Check the said number is Pandigital number or not? True Original number: 102345679 Check the said number is Pandigital number or not? False

n=int(input())
s=str(n)
digits=set(s)
if digits==set("0123456789"):
    print("Original number:",n)
    print("Check the said number is Pandigital number or not?",True)
else:
    print("Original number:",n)
    print("Check the said number is Pandigital number or not?",False)