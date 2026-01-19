# 	Write a Python program to calculate the sum of a list, after mapping each element to a value using the provided function.
# Sample Output: 20

def sum_after_mapping(lst, func):
    return sum(map(func, lst))

lst = list(map(int, input("Enter list elements: ").split()))

print("Choose mapping function:")
print("1. Double the value")
print("2. Square the value")
print("3. Increment by 1")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    func = lambda x: x * 2
elif choice == 2:
    func = lambda x: x * x
elif choice == 3:
    func = lambda x: x + 1
else:
    print("Invalid choice")
    exit()

result = sum_after_mapping(lst, func)
print(result)