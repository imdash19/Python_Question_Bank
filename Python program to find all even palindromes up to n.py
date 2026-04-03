# Write a Python program to find all even palindromes up to n.
# Output:
# Even palindromes up to 50 -
# [0, 2, 4, 6, 8, 22, 44]
# Even palindromes up to 100 -
# [0, 2, 4, 6, 8, 22, 44, 66, 88]
# Even palindromes up to 500 -
# [0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494]
# Even palindromes up to 2000 -
# [0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898]

n = int(input())

result = []

for i in range(n + 1):
    if i % 2 == 0 and str(i) == str(i)[::-1]:
        result.append(i)

print(f"Even palindromes up to {n} -")
print(result)