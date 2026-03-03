# Write a Python program that accepts six numbers as input and sorts them in descending order.
# Input: Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000). The six numbers are separated by a space.
# Input six integers: 15 30 25 14 35 40
# After sorting the said integers: 40 35 30 25 15 14

def accept_six_numbers():
    lst= [int(val) for val in input('Please enter your values separated with space: ').split()]

    lst.sort(reverse= True)
    for val in lst:
        print(val, end= '')
    return

accept_six_numbers()