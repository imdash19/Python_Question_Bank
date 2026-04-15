# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String: 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result: 'The lyrics is good!'
# 'The lyrics is poor!'

s = input()

not_pos = s.find("not")
poor_pos = s.find("poor")

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    s = s[:not_pos] + "good" + s[poor_pos + 4:]

print(s)