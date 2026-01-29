# Write a Python program that concatenates all elements in a list into a string and returns it.

# Write a Python program that concatenates all elements in a list into a string and returns it.

def concatinate_list_elements(lst):
    val = lst[0]
    for i in range(1, len(lst)):
        val += lst[i]
    return val

lst = [val for val in input('Please enter your elements separated with space: ').split()]
print('=' * 60)

print(concatinate_list_elements(lst))