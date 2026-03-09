# Write a Python program to calculate the maximum profit from selling and buying values of stock. An array of numbers represents the stock prices in chronological order.
# For example, given [8, 10, 7, 5, 7, 15], the function will return 10, since the buying value of the stock is 5 dollars and sell value is 15 dollars.
# Sample Input:
# ([8, 10, 7, 5, 7, 15])
# ([1, 2, 8, 1])
# ([])
# Sample Output:
# 10
# 7
# 0

s = input().strip()

if s in ["()", "[]", ""]:
    print(0)
else:
    a = list(map(int, s.strip("()[]").split(",")))
    if len(a) == 0:
        print(0)
    else:
        m = a[0]
        p = 0
        for i in a:
            if i < m:
                m = i
            if i - m > p:
                p = i - m
        print(p)