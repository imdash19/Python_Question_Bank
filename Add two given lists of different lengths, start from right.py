# Write a Python program to add two given lists of different lengths, start from right.
# Original lists: [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left: [2, 4, 10, 3, 4, 15]
# Original lists: [1, 2, 3, 4, 5, 6]
# [2, 4, -3]
# Add said two lists from left: [1, 2, 3, 6, 9, 3]

try:
    lst1 = [int(val) for val in input("Please enter your values for list1 separated with space: ").split()]
    print("="*60)
    lst2 = [int(val) for val in input("Please enter your values for list2 separated with space: ").split()]
    print("="*60)
    r1 = lst1[::-1]
    r2 = lst2[::-1]
    max_len = max(len(lst1), len(lst2))
    result = []

    for i in range(max_len):
        val1 = r1[i] if i < len(r1) else 0
        val2 = r2[i] if i < len(r2) else 0
        result.append(val1 + val2)

    result = result[::-1]

except ValueError:
    print("Please enter only integers...")
except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original lists: {lst1} \n {lst2}
Add said two lists from right: {result}""")