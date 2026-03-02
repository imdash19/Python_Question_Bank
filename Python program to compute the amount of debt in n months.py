# Write a Python program to compute the amount of debt in n months. Each month, the loan adds 5% interest to the $100,000 debt and rounds to the nearest 1,000 above.
# Input:
# An integer n (0 <= n <= 100)
# Input number of months: 7
# Amount of debt: $144000

def compute_debt():
    amount = 100000
    n = int(input("Input number of months: "))
    for _ in range(n):
        amount += amount * 0.05
        if amount % 1000 != 0:
            amount = ((amount // 1000) + 1) * 1000
    print("Amount of debt: $" + str(int(amount)))

compute_debt()