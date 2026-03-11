# Write a Python program to calculate the median from a list of numbers.
# Sample Input:
# [1,2,3,4,5]
# [1,2,3,4,5,6]
# [6,1,2,4,5,3]
# [1.0,2.11,3.3,4.2,5.22,6.55]
# [1.0,2.11,3.3,4.2,5.22]
# [2.0,12.11,22.3,24.12,55.22]
# Sample Output:
# 3
# 3.5
# 3.5
# 3.75
# 3.3
# 22.3

a=eval(input())
a=sorted(a)
n=len(a)

if n%2==1:
    m=a[n//2]
else:
    m=(a[n//2-1]+a[n//2])/2

if type(m)==float and m.is_integer():
    print(int(m))
else:
    print(m)