# Write a Python program to interleave two given list into another list randomly.
# Original lists: [1, 2, 7, 8, 3, 7]
# [4, 3, 8, 9, 4, 3, 8, 9]
# Interleave two given list into another list randomly: [4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]
import random

try:
    lst1= [int(val) for val in input("Please enter your values for list1 separated with space: ").split()]
    print("="*60)
    lst2= [int(val) for val in input("Please enter your values for list2 separated with space: ").split()]
    print("="*60)
    lst3= lst1 + lst2
    random.shuffle(lst3)

except Exception:
    print("Something went wrong! Please try again later.")

else:
    print(f"""Original lists: {lst1} \n {lst2}
Interleave two given list into another list randomly: {lst3}""")