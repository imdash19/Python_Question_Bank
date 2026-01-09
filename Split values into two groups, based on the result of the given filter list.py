# Write a Python program to split values into two groups, based on the result of the given filter list.
# Sample Output: [['red', 'green', 'pink'], ['blue']]

values = input("Enter values (space-separated): ").split()
filters = list(map(lambda x: x.lower() == 'true',
                   input("Enter filters (True/False space-separated): ").split()))

result = [
    [v for v, f in zip(values, filters) if f],
    [v for v, f in zip(values, filters) if not f]
]

print(result)