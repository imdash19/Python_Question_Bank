# 	Write a Python program to that takes any number of iterable objects or objects with a length property and returns the longest one.
# Sample Output: Green
#     [1, 2, 3, 4, 5]
#     [1, 2, 3, 4]

items = input("Enter iterable objects separated by | : ").split('|')

parsed_items = []
for item in items:
    item = item.strip()
    if item.startswith('[') and item.endswith(']'):
        parsed_items.append(eval(item))
    else:
        parsed_items.append(item)

longest = max(parsed_items, key=len)
print(longest)