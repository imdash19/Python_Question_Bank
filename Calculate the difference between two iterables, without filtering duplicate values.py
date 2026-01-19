# 	Write a Python program to calculate the difference between two iterables, without filtering duplicate values.
# Sample Output: [3]

def iterable_difference(iterable1, iterable2):
    return [x for x in iterable1 if x not in iterable2]

iterable1 = list(map(int, input("Enter first iterable elements: ").split()))
iterable2 = list(map(int, input("Enter second iterable elements: ").split()))

result = iterable_difference(iterable1, iterable2)
print(result)