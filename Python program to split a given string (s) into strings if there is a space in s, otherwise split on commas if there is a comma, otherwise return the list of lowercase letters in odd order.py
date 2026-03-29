# Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).
# Input:
# a b c d
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['a', 'b', 'c', 'd']
# Input:
# a,b,c,d
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['a', 'b', 'c', 'd']
# Input:
# abcd
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['b', 'd']

s = input().strip()

if ' ' in s:
    result = s.split()
elif ',' in s:
    result = s.split(',')
else:
    result = [ch for ch in s if (ord(ch) - ord('a')) % 2 == 1]

print(result)