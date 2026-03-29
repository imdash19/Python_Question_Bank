# Write a Python program to find strings in a given list containing a given substring.
# Input:
# [(ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# ['dog', 'donut', 'todo']
# Input:
# [(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# []

sub, words = input().strip()[1:-1].split(',', 1)
sub = sub.strip()
words = eval(words.strip())

result = [w for w in words if sub in w]
print(result)