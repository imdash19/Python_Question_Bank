# 	Write a Python program to cast the provided value as a list if it's not one.
# Sample Output: <class 'list'>
#     [1]
#     <class 'tuple'>
#     ['Red', 'Green']
#     <class 'set'>
#     ['Green', 'Red']
#     <class 'dict'>
#     [1, 2, 3]

def cast_as_list(val):
    return val if isinstance(val, list) else list(val)


val = eval(input('Please enter a value: '))
print('=' * 60)

print(type(val))
print(cast_as_list(val))