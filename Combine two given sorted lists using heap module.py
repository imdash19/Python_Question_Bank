# Write a Python program to combine two given sorted lists using heapq module.
# Original sorted lists: [1, 3, 5, 7, 9, 11] [0, 2, 4, 6, 8, 10]
# After merging the said two sorted lists: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
import heapq

try:
    lst1= [int(val) for val in input("Please enter your values for list1 separeted with space: ").split()]
    lst2 = [int(val) for val in input("Please enter your values for list2 separeted with space: ").split()]
    print("="*60)

except Exception:
    print("Something went wrong! Please try again later...")

else:
    print(f"""Original sorted lists: {lst1} \n {lst2}
After merging the said two sorted lists: {list(heapq.merge(lst1, lst2))}""")