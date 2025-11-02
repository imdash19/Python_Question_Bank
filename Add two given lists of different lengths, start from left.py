# Write a Python program to add two given lists of different lengths, start from left.
# Original lists: [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left: [5, 7, 6, 7, 5, 8]
# Original lists: [1, 2, 3, 4, 5, 6]
# [2, 4, -3]
# Add said two lists from left: [3, 6, 0, 4, 5, 6]

try:
    lst1= [int(val) for val in input("Please eter your values for list1 separated with space: ").split()]
    print("="*60)
    lst2 = [int(val) for val in input("Please eter your values for list2 separated with space: ").split()]
    print("="*60)
    max_len = max(len(lst1), len(lst2))
    result = []

    for i in range(max_len):
        val1 = lst1[i] if i < len(lst1) else 0
        val2 = lst2[i] if i < len(lst2) else 0
        result.append(val1 + val2)

except ValueError:
    print("Please don't enter ZERO / NEGATIVE NUMBER / ALPHABET / SPECIAL CHARACTER as input...")

except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original lists: {lst1} \n {lst2}
Add said two lists from left: {result}""")