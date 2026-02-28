# Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.
# Sample Data:
# Input third term of the series: 3
# Input 3rd last term: 3
# Input Sum of the series: 15
# Length of the series: 5
# Series: 1 2 3 4 5

def find_series():
    T3 = int(input("Input third term of the series: "))
    Tn_2 = int(input("Input 3rd last term: "))
    S = int(input("Input Sum of the series: "))

    n = (2 * S) // (T3 + Tn_2)
    d = (Tn_2 - T3) // (n - 5)
    a = T3 - 2 * d

    series = [a + i * d for i in range(n)]

    print("Length of the series:", n)
    print("Series:", *series)

find_series()