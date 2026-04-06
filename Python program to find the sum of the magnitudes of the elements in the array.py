# Write a Python program to find the sum of the magnitudes of the elements in the array. This sum should have a sign that is equal to the product of the signs of the entries.
# Input: [1, 3, -2]
# Output: -6
# Input: [1, -3, 3]
# Output: -7
# Input: [10, 32, 3]
# Output: 45
# Input: [-25, -12, -23]
# Output: -60

def get_sign(lst):
    res= 0
    for val in lst:
        if val < 0:
            res+= 1

    if res%2 == 0:
        return 1
    return -1

def get_sum_of_magnitudes(lst):
    sum= 0
    for val in lst:
        sum+= abs(val)
    return sum

lst= [int(val) for val in input().split()]
print(get_sign(lst) * get_sum_of_magnitudes(lst))