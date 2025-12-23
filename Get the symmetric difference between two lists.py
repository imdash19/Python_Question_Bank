# Write a Python program to get the symmetric difference between two lists,
# after applying the provided function to each list element of both.
# Sample Output: [1.2, 3.4]

def symmetric_difference_after_function(lst1, lst2, func):
    lst1 = list(map(func, lst1))
    lst2 = list(map(func, lst2))

    return list(set(lst1) ^ set(lst2))


try:
    lst1 = [1, 2, 3]
    lst2 = [2, 4]

    func = lambda x: x * 1.2

except Exception:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Output: {symmetric_difference_after_function(lst1, lst2, func)}''')