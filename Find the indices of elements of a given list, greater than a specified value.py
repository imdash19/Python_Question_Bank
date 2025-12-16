# Write a Python program to find the indices of elements of a given list, greater than a specified value.
# Original list: [1234, 1522, 1984, 19372, 1000, 2342, 7626]
# Indices of elements of the said list, greater than 3000 [3, 6]
# Original list: [1234, 1522, 1984, 19372, 1000, 2342, 7626]
# Indices of elements of the said list, greater than 20000 []

def find_index(lst,n):
    olst= []
    for i in range(len(lst)):
        if lst[i]>n:
            olst.append(i)
    return olst

try:
    lst= [int(val) for val in input('Please enter your list elements separated wwith space: ').split()]
    print('='*60)
    n= int(input('Please enter your number: '))
    print('='*60)

except ValueError:
    print('Please enter a number...')

except:
    print('Something went wrong :( Try again later...')

else:
    print(f'''Original list: {lst}
 Indices of elements of the said list, greater than {n}: {find_index(lst, n)}''')