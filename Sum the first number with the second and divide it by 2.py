# Sum a list of numbers. Write a Python program to sum the first number with the second and divide it by 2, then sum the second with the third and divide by 2, and so on.
# Original list: [1, 2, 3, 4, 5, 6, 7]
# Sum the said list of numbers: [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
# Original list: [0, 1, -3, 3, 7, -5, 6, 7, 11]
# Sum the said list of numbers: [0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]

def sum_two_consecutive_number_and_devide_by_two(lst):
    olst= []
    for i in range (len(lst)-1):
        val= (lst[i] + lst[i+1]) / 2
        olst.append(val)
    return olst

try:
    lst= [int(val) for val in input('Please enter your numbers separated ith space: ').split()]
    print('='*60)

except ValueError:
    print('Please enter numbers only...')

except:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Original list: {lst}
Sum the said list of numbers: {sum_two_consecutive_number_and_devide_by_two(lst)}''')