# Write a Python program that reads an integer n and finds the number of combinations of a, b, c and d (0 = a, b, c, d = 9) where (a + b + c + d) will be equal to n.
# Input:
# n (1 <= n <= 50)
# Input the number(n): 15
# Number of combinations: 592

n = int(input("Input the number(n): "))
count = 0

if 1 <= n <= 50:
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a + b + c + d == n:
                        count += 1
    print("Number of combinations:", count)
else:
    print("Invalid input")