# Write a Python program to find the longest string in a given list of strings.
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# center
# Input:
# ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# shatter

lst = eval(input())

longest = lst[0]

for s in lst:
    if len(s) > len(longest):
        longest = s

print(longest)