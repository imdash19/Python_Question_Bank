# Write a Python program to get a list of elements that exist in both lists,
# after applying the provided function to each list element of both.
# Sample Output: [2.1]

def get_common_elements_after_function(lst1, lst2, func):
    olst = []
    t1 = [func(val) for val in lst1]
    t2 = [func(val) for val in lst2]

    for val in t1:
        if val in t2 and val not in olst:
            olst.append(val)
    return olst


try:
    lst1 = [2.1, 3.5, 4.9, 5.2]
    lst2 = [1.0, 2.1, 6.8, 9.3]

except Exception:
    print('Something went wrong :( Please try again later...')

else:
    print(f'''Output:
{get_common_elements_after_function(lst1, lst2, lambda x: round(x, 1))}''')