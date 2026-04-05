# Write a Python program to find an integer exponent x such that a^x = n.
# Input: a = 2 : n = 1024
# Output: 10
# Input: a = 3 : n = 81
# Output: 4
# Input: a = 3 : n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849
# Output: 170

a = int(input())
n = int(input())

x = 0

while n > 1:
    n //= a
    x += 1

print(x)