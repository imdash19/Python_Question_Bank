# Write a Python program to count the number of arguments in a given function.
# Sample Input:
# ()
# (1)
# (1, 2)
# (1, 2, 3)
# (1, 2, 3, 4)
# [1, 2, 3, 4]
# Sample Output:
# 0
# 1
# 2
# 3
# 4
# 1

while True:
    try:
        s=input().strip()
        if s.startswith('('):
            t=eval(s)
            print(len(t))
        else:
            print(1)
    except:
        break