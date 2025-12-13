#  Write a Python program to find the specified number of largest products from two given list, multiplying an element from each list.
# Original lists: [1, 2, 3, 4, 5, 6]
# [3, 6, 8, 9, 10, 6]
# 3 Number of largest products from the said two lists: [60, 54, 50]
# 4 Number of largest products from the said two lists: [60, 54, 50, 48]

def find_the_specified_number_of_largest_products_from_two_given_list(lst1, lst2, n):
    olst= []
    for val1 in lst1:
        for val2 in lst2:
            olst.append(val1 * val2)
    olst.sort(reverse= True)
    return olst[:n]

try:
    lst1= [int(val) for val in input('Please enter your values for list1 separated with space: ').split()]
    print('='*60)

    lst2 = [int(val) for val in input('Please enter your values for list1 separated with space: ').split()]
    print('=' * 60)

    n= int(input('Please enter number of largest products from the two given lists: '))

except Exception:
    print('Something went wrong:( Please try again later...')

else:
    print(f'''Original lists: {lst1} {lst2}
{n} Number of largest products from the said two lists: {find_the_specified_number_of_largest_products_from_two_given_list(lst1, lst2, n)}''')