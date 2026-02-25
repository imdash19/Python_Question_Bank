# Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
# Sample data:
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70

X = list(map(int, input("Enter elements of array X separated by space: ").split()))
Y = list(map(int, input("Enter elements of array Y separated by space: ").split()))
Z = list(map(int, input("Enter elements of array Z separated by space: ").split()))
target = int(input("Enter target value: "))

found = False

print("\nCombinations whose sum equals", target, ":\n")

for x in X:
    for y in Y:
        for z in Z:
            if x + y + z == target:
                print(f"{x} + {y} + {z} = {target}")
                found = True

if not found:
    print("No combination found.")