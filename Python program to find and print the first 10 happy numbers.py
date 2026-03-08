# From Wikipedia,
# A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
# Write a Python program to find and print the first 10 happy numbers.
# Sample Input: [:10]
# Sample Output: [1, 7, 10, 13, 19, 23, 28, 31, 32, 44]

def happy(n):
    s=set()
    while n!=1 and n not in s:
        s.add(n)
        n=sum(int(i)**2 for i in str(n))
    return n==1

n=int(input()[1:])
res=[]
i=1
while len(res)<n:
    if happy(i):
        res.append(i)
    i+=1
print(res)