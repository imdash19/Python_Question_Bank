# 	Write a Python program to find the index of the last element in the given list that satisfies the provided testing function.
# Sample Output: 2

lst = list(map(int, input("Enter list elements: ").split()))

print("Choose condition:")
print("1. Even numbers")
print("2. Odd numbers")
print("3. Greater than a value")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    test_func = lambda x: x % 2 == 0
elif choice == 2:
    test_func = lambda x: x % 2 == 1
elif choice == 3:
    value = int(input("Enter comparison value: "))
    test_func = lambda x, v=value: x > v
else:
    print("Invalid choice")
    exit()

index = -1
for i in range(len(lst) - 1, -1, -1):
    if test_func(lst[i]):
        index = i
        break

print("Last matching index:", index)