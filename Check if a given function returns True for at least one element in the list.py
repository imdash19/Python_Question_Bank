# 	Write a Python program to check if a given function returns True for at least one element in the list.
# Sample Output: True
#     False

def test_function(x):
    return x % 2 == 0

lst = list(map(int, input("Enter list elements: ").split()))

result = any(test_function(x) for x in lst)

print(result)