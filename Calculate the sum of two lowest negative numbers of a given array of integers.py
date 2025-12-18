# Write a Python program to calculate the sum of two lowest negative numbers of a given array of integers.
# Original list elements: [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
# Sum of two lowest negative numbers of the said array of integers: -27
# Original list elements: [-4, 5, -2, 0, 3, -1, 4, 9]
# Sum of two lowest negative numbers of the said array of integers: -6

def sum_two_lowest_negative(lst):
    olst = []
    for val in lst:
        if val < 0:
            olst.append(val)
    olst.sort()
    val= olst[0] + olst[1]
    return val

try:
    lst= [int(val) for val in input('Please enter your values separated with space: ').split()]
    print('='*60)

except ValueError:
    print('Please enter numbers only...')

except:
    print('Something went wrong :( Please try again...')

else:
    print(f'''Original list elements: {lst}
 Sum of two lowest negative numbers of the said array of integers: {sum_two_lowest_negative(lst)}''')