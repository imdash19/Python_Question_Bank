# Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.
# Input: Value of n = 50
# Output: [[15, 1], [45, 1]]
# Input: Value of n = 65
# Output: [[15, 1], [45, 1], [54, 0]]
# Input
# Value of n = 75
# Output: [[15, 1], [45, 1], [54, 1]]
# Input: Value of n = 85
# Output: [[15, 1], [45, 1], [54, 1], [75, 1]]
# Input: Value of n = 150
# Output: [[15, 1], [45, 1], [54, 1], [75, 1], [105, 1], [135, 1]]

n= int(input('Please enter a number: '))
lst= []
for i in range(1, n):
    if i % 9 == 0 or i % 15 == 0:
        ilst= []
        cnt= str(i).count('5')
        if cnt:
            ilst.append(i)
            ilst.append(cnt)
            lst.append(ilst)

print(lst)