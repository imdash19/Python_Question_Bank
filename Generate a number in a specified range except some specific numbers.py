# Write a Python program to generate a number in a specified range except some specific numbers.
# Generate a number in a specified range (1, 10) except [2, 9, 10]: 7
# Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]: -4
import random

a= int(input("Please enter your starting range: "))
b= int(input("Please enter your ending range: "))
print("="*60)
lst= [int(val) for val in input("Please enter your number except you want: ").split()]
olst= []
for i in range(a, b):
    if i not in lst:
        olst.append(i)

print(f"Generate a number in a specified range ({a}, {b}) except {lst}: {random.choice(olst)}")