# Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations where the sum of the digits equals another given number (s). Do not use the same digits in a combination.
# Input: Two integers as number of combinations and their sum by a single space in a line. Input 0 0 to exit.
# Input number of combinations and sum, input 0 0 to exit:
# 5 6
# 2 4
# 0 0
# 2

def count_combinations():
    try:
        while True:
            n,s=map(int,input().split())
            if n==0 and s==0:
                break
            d=[0,1,2,3,4,5,6,7,8,9]
            c=0
            def f(i,k,t):
                nonlocal c
                if k==n:
                    if t==s:
                        c+=1
                    return
                for j in range(i,10):
                    f(j+1,k+1,t+d[j])
            f(0,0,0)
            print(c)
    except:
        pass

count_combinations()