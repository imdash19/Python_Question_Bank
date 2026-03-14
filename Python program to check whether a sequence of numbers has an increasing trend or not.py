# Write a Python program to check whether a sequence of numbers has an increasing trend or not.
# Sample Input:
# [1,2,3,4]
# [1,2,5,3,4]
# [-1,-2,-3,-4]
# [-4,-3,-2,-1]
# [1,2,3,4,0]
# Sample Output:
# True
# False
# False
# True
# False

s = input()
a = list(map(int, s.strip('[]').split(',')))

flag = True
for i in range(len(a)-1):
    if a[i] >= a[i+1]:
        flag = False
        break

print(flag)