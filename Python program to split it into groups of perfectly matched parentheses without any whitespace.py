# Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
# Input:
# ( ()) ((()()())) (()) ()
# Output:
# ['(())', '((()()()))', '(())', '()']
# Input:
# () (( ( )() ( )) ) ( ())
# Output:
# ['()', '((()()()))', '(())']

s = input()

res = []
temp = ''
count = 0

for ch in s:
    if ch == '(':
        temp += ch
        count += 1
    elif ch == ')':
        temp += ch
        count -= 1
        if count == 0:
            res.append(temp)
            temp = ''

print(res)