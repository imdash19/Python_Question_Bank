# Write a Python program to sum the first n positive integers.

def sum_first_n_integers():
    n= int(input('Please enter upto which positive number you want to sum: '))
    print('='*60)

    if n<=0:
        print('Please enter a positive integer')

    else:
        s= 0
        for i in range(1,n+1):
            s+=i
        print(f'The sum of first {n} positive number is: {s}')

sum_first_n_integers()