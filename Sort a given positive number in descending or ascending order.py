# Write a Python program to sort a given positive number in descending/ascending order.
# Descending -> Highest to lowest.
# Ascending -> Lowest to highest
# Original Number: 134543
# Descending order of the said number: 544331
# Ascending order of the said number: 133445
# Original Number: 43750973
# Descending order of the said number: 97754330
# Ascending order of the said number: 3345779

def sort_positive_ascending_order(lst):
    lst.sort()
    i= ''
    for val in lst:
        i+= str(val)
    return int(i)

def sort_positive_descending_order(lst):
    lst.sort(reverse= True)
    i= ''
    for val in lst:
        i += str(val)
    return int(i)

try:
    lst= []
    n= int(input('Please enter a positive number: '))
    if n < 0:
        raise ValueError('Please enter a positive number...')

    val= ''
    for i in range(len(str(n))):
        lst.append(int(str(n)[i]))

except ValueError:
    print('Please enter numers inly...')

else:
    print(f'''Original Number: {n}
 Descending order of the said number: {sort_positive_descending_order(lst)}
 Ascending order of the said number: {sort_positive_ascending_order(lst)}''')