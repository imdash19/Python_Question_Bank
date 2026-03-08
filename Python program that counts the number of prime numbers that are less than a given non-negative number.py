# Write a Python program that counts the number of prime numbers that are less than a given non-negative number.
# Sample Input:
# (10)
# (100)
# Sample Output:
# 4
# 25

n=int(input())
if n<2:
    print(0)
else:
    p=[True]*n
    p[0]=p[1]=False
    for i in range(2,int(n**0.5)+1):
        if p[i]:
            for j in range(i*i,n,i):
                p[j]=False
    print(sum(p))