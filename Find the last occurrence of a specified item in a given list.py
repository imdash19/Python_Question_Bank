# Write a Python program to find the last occurrence of a specified item in a given list.
# Original list: ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of ‘f’ in the said list: 7
# Last occurrence of ‘c’ in the said list: 15
# Last occurrence of ‘k’ in the said list: 14
# Last occurrence of ‘w’ in the said list: 12

try:
    lst= [val for val in input("Please enter your values separated with space: ").split()]
    print("="*60)
    ch= input("Please enter your choice to find it's last occurance: ")
    print("="*60)

except Exception:
    print("Something went wrong! Try again later...")

else:
    if ch in lst:
        print(f"Last occurrence of {ch} in the said list: {len(lst)-1-lst[::-1].index(ch)}")
    else:
        print(f"{ch} isn't available in the said list.")