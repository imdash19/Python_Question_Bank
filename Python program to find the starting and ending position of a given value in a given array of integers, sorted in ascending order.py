# Write a Python program to find the starting and ending position of a given value in a given array of integers, sorted in ascending order.
# If the target is not found in the array, return [0, 0].
# Input: [5, 7, 7, 8, 8, 8] target value = 8
# Output: [3, 5]
# Input: [1, 3, 6, 9, 13, 14] target value = 4
# Output: [0, 0]

def get_first_last_index():
    lst= [int(val) for val in input('Please enter your array of integers separated with space: ').split()]
    print('='*60)

    n= int(input('Please enter your target value: '))
    print('='*60)

    olst= [0, 0]

    if n in lst:
        if lst.count(n) == 1:
            olst[-1]= lst.index(n)
            return olst

        else:
            olst[0]= lst.index(n)
            for i in range(len(lst)-1, olst[0], -1):
                if lst[i] == n:
                    olst[-1] = i
                    break

            return olst

    else:
        return olst

print(get_first_last_index())