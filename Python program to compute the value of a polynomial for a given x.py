# Write a Python program to compute the value of a polynomial for a given x.
# The program should ask the user to enter the coefficients of the polynomial, separated by spaces.
# Then, it should ask for the value of x.
# Use Python’s sum() function and list comprehension to calculate the polynomial efficiently
# Each term of the polynomial is calculated as:
# term=coefficient*x^power
# Display the final result clearly.
# Hint:
# The coefficients are entered in order of decreasing powers of x.
# For example, the polynomial 
# 2x^3+3x^2+x+5 has coefficients 2 3 1 5.

def evaluate_polynomial(coefficients, x):
    n = len(coefficients)
    
    result = sum(
        coefficients[i] * (x ** (n - i - 1))
        for i in range(n)
    )
    
    return result

if __name__ == "__main__":
    coefficients = list(map(int, input().split()))
    x = int(input())
    
    print('Polynomial value: ', evaluate_polynomial(coefficients, x))
