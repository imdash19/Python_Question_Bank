# 	Write a Python program to check if a given function returns True for every element in a list.
# Sample Output: True
#     False
#     False

lst = list(map(int, input("Enter list elements: ").split()))

print("Choose a condition:")
print("1. Check if all elements are even")
print("2. Check if all elements are positive")
print("3. Check if all elements are greater than a given number")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    result = all(x % 2 == 0 for x in lst)

elif choice == 2:
    result = all(x > 0 for x in lst)

elif choice == 3:
    n = int(input("Enter the number to compare with: "))
    result = all(x > n for x in lst)

else:
    result = False

print(result)