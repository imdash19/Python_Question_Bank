# Write a Python program to check common elements between two given list are in same order or not.
# Original lists: ['red', 'green', 'black', 'orange']
# ['red', 'pink', 'green', 'white', 'black']
# ['white', 'orange', 'pink', 'black']
# Test common elements between color1 and color2 are in same order: True
# Test common elements between color1 and color3 are in same order: False
# Test common elements between color2 and color3 are in same order: False

lst = []
n = int(input("Please enter how many lists you want to enter: "))

for i in range(n):
    print("=" * 60)
    print(f"Inside list {i + 1}")
    print("=" * 60)
    slst = [val for val in input("Please enter your values separated with space: ").split()]
    lst.append(slst)

print("\nOriginal lists:")
for i in lst:
    print(i)

print()
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        first = lst[i]
        second = lst[j]
        common = [val for val in first if val in second]
        seq1 = [val for val in first if val in common]
        seq2 = [val for val in second if val in common]
        result = (seq1 == seq2)
        print(f"Test common elements between list{i+1} and list{j+1} are in same order: {result}")